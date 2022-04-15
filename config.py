import os

class Config(object):
    # get a token from @BotFather
    TG_BOT_TOKEN = "5249699526:AAF0nosC8D4MhqBQtsNGC8ux82WTgGVLvlg"
    # The Telegram API things
    APP_ID = 3796974
    API_HASH = "9511d0112631f9990337eb724d1a7d0d"
    # Update channel for Force Subscribe
    UPDATE_CHANNEL = os.environ.get("UPDATE_CHANNEL", "latest_tvserials_first_on_net")
    # log channel
    LOG_CHANNEL = os.environ.get("LOG_CHANNEL", "mjfileupload")
    # Get these values from my.telegram.org
    CHAT_ID = os.environ.get("CHAT_ID", "zeemarathiserials2")
    # Array to store users who are authorized to use the bot
    AUTH_USERS = "1464063686"
    # Banned Unwanted Members..
    BANNED_USERS = []
    # the download location, where the HTTP Server runs
    DOWNLOAD_LOCATION = "./DOWNLOADS"
    # Telegram maximum file upload size
    MAX_FILE_SIZE = 50000000
    TG_MAX_FILE_SIZE = 2097152000
    FREE_USER_MAX_FILE_SIZE = 50000000
    # chunk size that should be used with requests
    CHUNK_SIZE = int(os.environ.get("CHUNK_SIZE", 128))
    # default thumbnail to be used in the videos
    DEF_THUMB_NAIL_VID_S = os.environ.get("DEF_THUMB_NAIL_VID_S", "https://placehold.it/90x90")
    # proxy for accessing youtube-dl in GeoRestricted Areas
    # Get your own proxy from https://github.com/rg3/youtube-dl/issues/1091#issuecomment-230163061
    HTTP_PROXY = os.environ.get("HTTP_PROXY", "")
    # https://t.me/hevcbay/951
    OUO_IO_API_KEY = ""
    # maximum message length in Telegram
    MAX_MESSAGE_LENGTH = 4096
    # set timeout for subprocess
    PROCESS_MAX_TIMEOUT = 3600
    # watermark file
    DEF_WATER_MARK_FILE = ""
    # Database url
    DB_URI = "postgres://nrhsxjexkycakn:5a97936bd10f2a9dae38105279f5faff20ec08fca55ef42b37a478b438a742ca@ec2-52-48-159-67.eu-west-1.compute.amazonaws.com:5432/d8jnslcpc51j8f"
    
