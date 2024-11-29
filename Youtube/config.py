import os

class Config(object):
     
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "7699344679:AAGp_xEKvmnNvj5myPwwsNwIsXxg2BNH-NU")
    API_ID = int(os.environ.get("API_ID", "28800808"))
    API_HASH = os.environ.get("API_HASH","b0a58c6d13e8077fe839985258b9b0be")
    #Add your channel id. For force Subscribe.
    CHANNEL = os.environ.get("CHANNEL", "https://t.me/STRIKERBOY_SUPPORT")
    #Skip or add your proxy from https://github.com/rg3/youtube-dl/issues/1091#issuecomment-230163061
    HTTP_PROXY = ''
