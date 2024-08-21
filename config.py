import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# Get this value from my.telegram.org/apps
API_ID = int(getenv("API_ID", "28542531"))
API_HASH = getenv("API_HASH", "9f4889cd2437d72ede20428c07a909be")

# Get your token from @BotFather on Telegram.
BOT_TOKEN = getenv("BOT_TOKEN", "5663640542:AAEdpagTHhnPA2lC-SECoUU3mBv8oajuNy0")

# Get your mongo url from cloud.mongodb.com
MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://pikachu:randi@cluster0.tndvlel.mongodb.net/?retryWrites=true&w=majority")

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 9999999999999))

# Chat id of a group for logging bot's activities
LOGGER_ID = int(getenv("LOGGER_ID", "-1001772857132"))

# Get this value from @FallenxBot on Telegram by /id
OWNER_ID = int(getenv("OWNER_ID", "6045293810"))
OWNER_USERNAME = getenv("OWNER_USERNAME","shaeep43")

## Fill these variables if you're deploying on heroku.
# Your heroku app name
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
# Get it from http://dashboard.heroku.com/account
HEROKU_API_KEY = getenv("HEROKU_API_KEY")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/IR-O/Irone",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "master")
GIT_TOKEN = getenv(
    "GIT_TOKEN", None
)  # Fill this variable if your upstream repository is private

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/iro_bot_support")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/iro_x_support")

# Set this to True if you want the assistant to automatically leave chats after an interval
AUTO_LEAVING_ASSISTANT = getenv("AUTO_LEAVING_ASSISTANT", "True")


# Get this credentials from https://developer.spotify.com/dashboard
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", "6df6e890c5bb46c6b8e760c7080b6688")
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", "b97aee71f3f34056a3ceb3fcf33f3a53")


# Maximum limit for fetching playlist's track from youtube, spotify, apple links.
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))


# Telegram audio and video file size limit (in bytes)
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 104857600))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 1048574951424))
# Checkout https://www.gbmb.org/mb-to-bytes for converting mb to bytes


# Get your pyrogram v2 session from @StringFatherBot on Telegram
STRING1 = getenv("STRING_SESSION", "BQE07uIABx_8NKi8S41mNgWFsFL2wgv3k8I2sF9GvUE67zuUx42ezm7dz2pepspHC9tk-HBahgvQ295n9QeUJKLytG0vYf7TcO_LWuokDokEMtkFRo0Kl9YFjBBJS0BaiEfxS-7fQFQ_QWs_jg9c1eTvcbjtKM1bIdWX0845uu-RL5twyDHClaiAExYOur8AC15EM7P63Wyfib3Doyu2vG-EV_WmHLvyyc8mpTgiy7R5eeaotr_y-S5QjFgPKz5E6k7JIVQpVZE3lfgDY5GLJg8hsCWZ2sMrw9uMrITbZLZxWJc0j01EJv4NhYkrAET9yF0OpR8_I-4i6iSNNRNCS3XmidY5JgAAAAHAuDpVAA")
STRING2 = getenv("STRING_SESSION2", "BQE07uIAeIIr9sL6m9UPz1GAOaMx5p_D_vsJYjUxplSdJIMwZA8ICMZfzzlKK3z0TPc4bY_DMJsedQcGDxCiV_JfMHopqztOV9E7L7mhHVNSxrJVGR_TUzmf2rJ-nJsUoENePVVubp1yOkY00SdiQLiZ2sxCwRu8BFdNkzThQfPL2iGeWGgHWO5mGRsgYJomQgHBRqDXlGQ94qoMt9HkE8O_i9H-tdWbjWBkiN2LEQuyRXjAZGH0YN7pcioaK68OBIhKkOIZZmOy5Yvf7uXuUEjNnD-OGNVnEvCFDs0LCrfHuq0kI4llt2a27nmwxAs7sBIeLdWjnaSpPS6YzSdXfXiNEy5oBwAAAAGxC4UDAA")
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)


BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}


START_IMG_URL = getenv(
    "START_IMG_URL", "https://te.legra.ph/file/7c8a61882e4d9f5cf8f58.jpg"
)
PING_IMG_URL = getenv(
    "PING_IMG_URL", "https://te.legra.ph/file/b8a0c1a00db3e57522b53.jpg"
)
PLAYLIST_IMG_URL = "https://te.legra.ph/file/4ec5ae4381dffb039b4ef.jpg"
STATS_IMG_URL = "https://te.legra.ph/file/e906c2def5afe8a9b9120.jpg"
TELEGRAM_AUDIO_URL = "https://te.legra.ph/file/6298d377ad3eb46711644.jpg"
TELEGRAM_VIDEO_URL = "https://te.legra.ph/file/6298d377ad3eb46711644.jpg"
STREAM_IMG_URL = "https://te.legra.ph/file/bd995b032b6bd263e2cc9.jpg"
SOUNCLOUD_IMG_URL = "https://te.legra.ph/file/bb0ff85f2dd44070ea519.jpg"
YOUTUBE_IMG_URL = "https://te.legra.ph/file/6298d377ad3eb46711644.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://te.legra.ph/file/37d163a2f75e0d3b403d6.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://te.legra.ph/file/b35fd1dfca73b950b1b05.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://te.legra.ph/file/95b3ca7993bbfaf993dcb.jpg"


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))


if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_CHAT:
    if not re.match("(?:http|https)://", SUPPORT_CHAT):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHAT url is wrong. Please ensure that it starts with https://"
        )
