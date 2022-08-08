import os
from contextlib import suppress
from typing import Optional

from dotenv import load_dotenv


def init_log() -> Optional[int]:
    if (log_group := os.environ.get("LOG_GROUP")) is not None:
        with suppress(ValueError):
            return int(log_group)
    return None


def init_request_timeout() -> int:
    if (request_timeout := os.environ.get("REQUEST_TIMEOUT", "30")) is not None:
        with suppress(ValueError):
            return int(request_timeout)


if os.path.isfile("config.env"):
    load_dotenv("config.env")


class Config:
    BOT_TOKEN = os.environ["BOT_TOKEN","5598969538:AAF-oqjulil42ZGk9PQ6nbYkOrPZDaOMnk8"]
    API_ID = int(os.environ["API_ID","4682685"])
    API_HASH = os.environ["API_HASH","3eba5d471162181b8a3f7f5c0a23c307"]
    EXEC_PATH = os.environ.get("GOOGLE_CHROME_SHIM", None)
    # OPTIONAL
    LOG_GROUP = init_log()
    REQUEST_TIMEOUT = init_request_timeout()
    SUPPORT_GROUP_LINK = os.environ.get("SUPPORT_GROUP", "https://t.me/+Ut3otVo52AQzMTc1")
