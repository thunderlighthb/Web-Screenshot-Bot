# (c) AlenPaulVarghese
# -*- coding: utf-8 -*-

import os

from config import Config
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from webshotbot import WebshotBot


@WebshotBot.on_message(
    filters.regex(pattern="http[s]*://.+")
    & filters.private
    & ~filters.create(lambda _, __, m: bool(m.edit_date))
)
async def checker(client: WebshotBot, message: Message):
    msg = await message.reply_text("working", True)
    markup = []
    _settings = client.get_settings_cache(message.chat.id)
    if _settings is None:
        _settings = dict(
            type="pdf",
            fullpage=True,
            scroll_control="no",
            resolution="800x600",
            split=False,
        )
    markup.extend(
        [
            [
                InlineKeyboardButton(
                    text=f"Format - {_settings['type'].upper()}",
                    callback_data="format",
                )
            ],
            [
                InlineKeyboardButton(
                    text=f"Page - {'Full' if _settings['fullpage'] else 'Partial'}",
                    callback_data="page",
                )
            ],
            [
                InlineKeyboardButton(
                    text=f"Scroll Site - {_settings['scroll_control'].title()}",
                    callback_data="scroll",
                )
            ],
        ]
    )
    _split = _settings["split"]
    _resolution = _settings["resolution"]
    if _split or "600" not in _resolution:
        markup.extend(
            [
                [
                    InlineKeyboardButton(
                        text="hide additional options ˄", callback_data="options"
                    )
                ],
                [
                    InlineKeyboardButton(
                        text=f"resolution | {_resolution}", callback_data="res"
                    ),
                ],
                [
                    InlineKeyboardButton(
                        text=f"Split - {'Yes' if _split else 'No'}",
                        callback_data="splits",
                    )
                ]
                if _settings["type"] != "pdf"
                else [],
                [
                    InlineKeyboardButton(
                        text="▫️ site statitics ▫️", callback_data="statics"
                    )
                ],
            ]
        )
    else:
        markup.append(
            [
                InlineKeyboardButton(
                    text="show additional options ˅", callback_data="options"
                )
            ]
        )
    markup.extend(
        [
            [InlineKeyboardButton(text="▫️ start render ▫️", callback_data="render")],
            [InlineKeyboardButton(text="cancel", callback_data="cancel")],
        ]
    )
    await msg.edit(
        text="Choose the prefered settings",
        reply_markup=InlineKeyboardMarkup(markup),
    )


@WebshotBot.on_message(filters.command(["start"]))
async def start(_, message: Message) -> None:
    await message.reply_text(
        f"<b>Hi {message.from_user.first_name} 👋\n"
        "𝑰 𝒄𝒂𝒏 𝑺𝒄𝒓𝒆𝒆𝒏𝑺𝒉𝒐𝒕  𝒘𝒆𝒃𝒔𝒊𝒕𝒆 𝒐𝒇 𝒂 𝒈𝒊𝒗𝒆𝒏 𝒍𝒊𝒏𝒌 𝒕𝒐 𝒆𝒊𝒕𝒉𝒆𝒓 𝑷𝑫𝑭 𝒐𝒓 𝑷𝑵𝑮/𝑱𝑷𝑬𝑮 \n 𝑱𝒖𝒔𝒕 𝒔𝒆𝒏𝒅 𝒂 𝒍𝒊𝒏𝒌 𝒂𝒏𝒅 𝒔𝒆𝒆 𝒎𝒚 𝒑𝒐𝒘𝒆𝒓</b>",
        quote=True,
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("❓ About", callback_data="about_cb")]]
        ),
    )


@WebshotBot.on_message(filters.command(["about", "feedback"]))
async def feedback(_, message: Message) -> None:
    await message.reply_text(
        text="𝙒𝙀𝘽𝙎𝙄𝙏𝙀 𝙎𝘾𝙍𝙀𝙀𝙉𝙎𝙃𝙊𝙏 𝘽𝙊𝙏 \n 𝙁𝙚𝙖𝙩𝙪𝙧𝙚𝙨 ❤️ \n 👉𝙋𝙙𝙛,𝙥𝙣𝙜,𝙟𝙥𝙚𝙜 \n👉𝙍𝙚𝙨𝙤𝙡𝙪𝙩𝙞𝙤𝙣 \n👉𝙁𝙪𝙡𝙡 𝙨𝙞𝙩𝙚 \n👉𝘼𝙪𝙩𝙤 𝙨𝙘𝙧𝙤𝙡𝙡/𝙢𝙖𝙣𝙪𝙖𝙡",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Oᗯᑎᗴᖇ",
                        url="https://t.me/fligher",
                    ),
                    InlineKeyboardButton(
                        "ⓄⓌⓃⒺⓇ",
                        url="https://t.me/v_ec_na",
                    ),
                ],
                [
                    InlineKeyboardButton(
                        "𝙏𝙍𝙐𝙈𝘽𝙊𝙏𝙎",
                        url="https://t.me/movie_time_botonly",
                    )
                ],
            ]
        ),
    )


@WebshotBot.on_message(
    filters.command(["support", "feedback", "help"])& filters.private
)
async def help_handler(_, message: Message) -> None:
     if Config.SUPPORT_GROUP_LINK is not None:    
        await message.reply_text(
            "__Frequently Asked Questions__** : -\n\n"
            "A. How to use the bot to render a website?\n\n"
            "Ans:** Send the link of the website you want to render, "
            "choose the desired setting, and click `start render`.\n\n"
            "**B. How does this bot work?\n\n Ans:** This bot uses"
            " an actual browser under the hood to render websites.\n\n"
            "**C. How to report a bug or request a new feature?\n\n"
            "Ans:** For feature requests or bug reports, @V_ec_na ",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            text="Support group", url=Config.SUPPORT_GROUP_LINK
                        )
                    ]
                ]
            ),
            disable_web_page_preview=True,
        )


@WebshotBot.on_message(filters.command(["debug", "log"]) & filters.private)
async def send_log(_, message: Message) -> None:
    try:
        sudo_user = int(os.environ["SUDO_USER"])
        if sudo_user != message.chat.id:
            raise Exception
    except Exception:
        return
    if os.path.exists("debug.log"):
        await message.reply_document("debug.log")
    else:
        await message.reply_text("file not found")
