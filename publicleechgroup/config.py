import os
import sys

from dotenv import load_dotenv
from .get_cfg import get_config


# apparently, no error appears even if the path does not exists
load_dotenv("config.env")


class Config:
    # get a token from @BotFather
    TG_BOT_TOKEN = "1783024258:AAGKpo5NOmOE2Tnd8mK9PvH3mKw3TQPmFpA"
    # The Telegram API things
    APP_ID = 2532603
    API_HASH = "f565b00bbe3ad9c6748e39a3a71d16e7"
    # Get these values from my.telegram.org
    # array to store the channel ID who are authorized to use the bot
    AUTH_CHANNEL = [-1001399288270]
    
    # the download location, where the HTTP Server runs
    DOWNLOAD_LOCATION = "/"
    # Telegram maximum file upload size
    MAX_FILE_SIZE = 2097152000
    TG_MAX_FILE_SIZE = 2097152000
    FREE_USER_MAX_FILE_SIZE = 2097152000
        
    # chunk size that should be used with requests
    CHUNK_SIZE = 3120
    # default thumbnail to be used in the videos
    DEF_THUMB_NAIL_VID_S = get_config(
        "DEF_THUMB_NAIL_VID_S",
        "https://telegra.ph/file/8b973b270f4f380a427b1.png"
    )
    # maximum message length in Telegram
    MAX_MESSAGE_LENGTH = int(get_config(
        "MAX_MESSAGE_LENGTH",
        4096
    ))
    # set timeout for subprocess
    PROCESS_MAX_TIMEOUT = int(get_config(
        "PROCESS_MAX_TIMEOUT",
        3600
    ))
    #
    ARIA_TWO_STARTED_PORT = int(get_config(
        "ARIA_TWO_STARTED_PORT",
        6800
    ))
    EDIT_SLEEP_TIME_OUT = int(get_config(
        "EDIT_SLEEP_TIME_OUT",
        1
    ))
    MAX_TIME_TO_WAIT_FOR_TORRENTS_TO_START = int(get_config(
        "MAX_TIME_TO_WAIT_FOR_TORRENTS_TO_START",
        600
    ))
    MAX_TG_SPLIT_FILE_SIZE = int(get_config(
        "MAX_TG_SPLIT_FILE_SIZE",
        1900000000
    ))
    # add config vars for the display progress
    FINISHED_PROGRESS_STR = get_config("FINISHED_PROGRESS_STR", "█")
    UN_FINISHED_PROGRESS_STR = get_config("UN_FINISHED_PROGRESS_STR", "░")
    # add offensive API
    TG_OFFENSIVE_API = get_config("TG_OFFENSIVE_API", None)
    # URL for the rclone configuration
    R_CLONE_CONF_URI = "https://t.me/publicleech689/7734"
    # Destination folder for the rclone
    R_CLONE_DEST = "/TorToolKitLeech"
    # because, https://t.me/c/1494623325/5603
    SHOULD_USE_BUTTONS = "True"
    #
    LOG_FILE_ZZGEVC = get_config("LOG_FILE_ZZGEVC", "TorToolKit.log")
    #
    SP_LIT_ALGO_RITH_M = get_config(
        "SP_LIT_ALGO_RITH_M",
        "rar"
    )
    #
    DIS_ABLE_ST_GFC_COMMAND_I = get_config(
        "DIS_ABLE_ST_GFC_COMMAND_I",
        False
    )
    #
    SLEEP_THRES_HOLD = get_config(
        "SLEEP_THRES_HOLD",
        98712
    )
    # array to store the users who will have control (permissions)
    # in the bot
    SUDO_USERS = [1338936440,1002182448,754495556]
