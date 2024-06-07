from pyrogram import Client
import os

TOKEN = os.environ.get("6611635702:AAG-Kf2PpPJOHoXqmGNu35bwYJgQ4qx39oI", "")

API_ID = int(os.environ.get("27357662", ""))

API_HASH = os.environ.get("08659ac028beec1c95073c1964298f36", "")

if __name__ == "__main__" :
    plugins = dict(
        root="plugins"
    )
    app = Client(
        "renamer",
        bot_token=TOKEN,
        api_id=API_ID,
        api_hash=API_HASH,
        plugins=plugins
    )
    app.run()
