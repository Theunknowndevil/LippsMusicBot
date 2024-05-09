import re
import os
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# Get this value from my.telegram.org/apps
API_ID = int(getenv("24598821"))
API_HASH = getenv("ad13216ba888b295d369885a1da2295f")

# Get your token from @BotFather on Telegram.
BOT_TOKEN = getenv("6559067376:AAHs459BLwW9wybgtkJieq60sZDM9x8-uCc",None) 

# A name for your Music bot.
MUSIC_BOT_NAME = getenv("MUSIC_BOT_NAME", "Ax Muzic Bot")

# Get your mongo url from cloud.mongodb.com
MONGO_DB_URI = getenv("mongodb+srv://mashishkumar108:mashishkuma107@cluster0.4gqbfqf.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0", None)

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 300))

# Chat id of a group for logging bot's activities
#LOG_ID = int(getenv("LOG_ID", "-1001957871522"))
LOGGER_ID = int(getenv("1002060417665", None))

# Get this value from @RoseBot on Telegram by /id
OWNER_ID = int(getenv("5032639872", "2101893551"))

## Fill these variables if you're deploying on heroku.
# Your heroku app name
HEROKU_APP_NAME = getenv("axmuzicbot")
# Get it from http://dashboard.heroku.com/account
HEROKU_API_KEY = getenv("HRKU-0ce15417-d487-47b4-9144-fcb533f615ec")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/Lippsxd/LippsMusicBot",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "lippsxd")
GIT_TOKEN = getenv(
    "GIT_TOKEN", None
)  # Fill this variable if your upstream repository is private

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/i7cloudsstatus")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/GN807")

# Set this to True if you want the assistant to automatically leave chats after an interval
AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", False))

#Auto Gcast/Broadcast Handler (True = broadcast on , False = broadcast off During Hosting, Dont Do anything here.)
AUTO_GCAST = os.getenv("AUTO_GCAST","True")

#Auto Broadcast Message That You Want Use In Auto Broadcast In All Groups.
AUTO_GCAST_MSG = getenv("AUTO_GCAST_MSG", "")

# Get this credentials from https://developer.spotify.com/dashboard
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", None)
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", None)


# Maximum limit for fetching playlist's track from youtube, spotify, apple links.
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))


# Telegram audio and video file size limit (in bytes)
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 104857600))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 1073741824))
# Checkout https://www.gbmb.org/mb-to-bytes for converting mb to bytes


# Get your pyrogram v2 session from @StringFatherBot on Telegram
STRING1 = getenv("BQF3WSUAHbq7atjT_JyNr5na6c2FprEkI3vG7FVRl9zw6CyuUDwxoZ_tHjSBCyCbAhPH5niA_lrj2PpbLH6aUbvlZR1mtQ7cHA0STLZMrcuXD3awpvs2Lm0HzGkme7bVUj_lhO5jAGSmuiy-04ur6v68KAGqeQtzMJQwg54i9EcEcxhbzNheCAL-NB-x3X4GI4GsEXKGwSpn0l5K6l-ZWr4gVGImCSLeCgtp091b7P7yV6o4w3hWhQsrnuyLQFhduhPW2tZmUiyL7xpGSlMSYejP7pdDhDO2J94vm616uyhuDe5eBlssvSa65KPoDqpUUfKPmchA6fZrhv7o532YmVm3es2FBgAAAAEr9_2AAA", None)
STRING2 = getenv("BQF3WSUAHbq7atjT_JyNr5na6c2FprEkI3vG7FVRl9zw6CyuUDwxoZ_tHjSBCyCbAhPH5niA_lrj2PpbLH6aUbvlZR1mtQ7cHA0STLZMrcuXD3awpvs2Lm0HzGkme7bVUj_lhO5jAGSmuiy-04ur6v68KAGqeQtzMJQwg54i9EcEcxhbzNheCAL-NB-x3X4GI4GsEXKGwSpn0l5K6l-ZWr4gVGImCSLeCgtp091b7P7yV6o4w3hWhQsrnuyLQFhduhPW2tZmUiyL7xpGSlMSYejP7pdDhDO2J94vm616uyhuDe5eBlssvSa65KPoDqpUUfKPmchA6fZrhv7o532YmVm3es2FBgAAAAEr9_2AAA", None)
STRING3 = getenv("BQF3WSUAHbq7atjT_JyNr5na6c2FprEkI3vG7FVRl9zw6CyuUDwxoZ_tHjSBCyCbAhPH5niA_lrj2PpbLH6aUbvlZR1mtQ7cHA0STLZMrcuXD3awpvs2Lm0HzGkme7bVUj_lhO5jAGSmuiy-04ur6v68KAGqeQtzMJQwg54i9EcEcxhbzNheCAL-NB-x3X4GI4GsEXKGwSpn0l5K6l-ZWr4gVGImCSLeCgtp091b7P7yV6o4w3hWhQsrnuyLQFhduhPW2tZmUiyL7xpGSlMSYejP7pdDhDO2J94vm616uyhuDe5eBlssvSa65KPoDqpUUfKPmchA6fZrhv7o532YmVm3es2FBgAAAAEr9_2AAA", None)
STRING4 = getenv("BQF3WSUAHbq7atjT_JyNr5na6c2FprEkI3vG7FVRl9zw6CyuUDwxoZ_tHjSBCyCbAhPH5niA_lrj2PpbLH6aUbvlZR1mtQ7cHA0STLZMrcuXD3awpvs2Lm0HzGkme7bVUj_lhO5jAGSmuiy-04ur6v68KAGqeQtzMJQwg54i9EcEcxhbzNheCAL-NB-x3X4GI4GsEXKGwSpn0l5K6l-ZWr4gVGImCSLeCgtp091b7P7yV6o4w3hWhQsrnuyLQFhduhPW2tZmUiyL7xpGSlMSYejP7pdDhDO2J94vm616uyhuDe5eBlssvSa65KPoDqpUUfKPmchA6fZrhv7o532YmVm3es2FBgAAAAEr9_2AAA", None)
STRING5 = getenv("BQF3WSUAHbq7atjT_JyNr5na6c2FprEkI3vG7FVRl9zw6CyuUDwxoZ_tHjSBCyCbAhPH5niA_lrj2PpbLH6aUbvlZR1mtQ7cHA0STLZMrcuXD3awpvs2Lm0HzGkme7bVUj_lhO5jAGSmuiy-04ur6v68KAGqeQtzMJQwg54i9EcEcxhbzNheCAL-NB-x3X4GI4GsEXKGwSpn0l5K6l-ZWr4gVGImCSLeCgtp091b7P7yV6o4w3hWhQsrnuyLQFhduhPW2tZmUiyL7xpGSlMSYejP7pdDhDO2J94vm616uyhuDe5eBlssvSa65KPoDqpUUfKPmchA6fZrhv7o532YmVm3es2FBgAAAAEr9_2AAA", None)


BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}


START_IMG_URL = getenv("START_IMG_URL", "https://graph.org/file/b8666bc80cf6b0fcfa6d4.jpg")

PING_IMG_URL = getenv(
    "PING_IMG_URL",
    "LippsMusic/assets/Ping.jpeg",
)

PLAYLIST_IMG_URL = getenv(
    "PLAYLIST_IMG_URL",
    "LippsMusic/assets/Playlist.jpeg",
)

GLOBAL_IMG_URL = getenv(
    "GLOBAL_IMG_URL",
    "LippsMusic/assets/Global.jpeg",
)

STATS_IMG_URL = getenv(
    "STATS_IMG_URL",
    "LippsMusic/assets/Stats.jpeg",
)

TELEGRAM_AUDIO_URL = getenv(
    "TELEGRAM_AUDIO_URL",
    "LippsMusic/assets/Audio.jpeg",
)

TELEGRAM_VIDEO_URL = getenv(
    "TELEGRAM_VIDEO_URL",
    "LippsMusic/assets/Video.jpeg",
)

STREAM_IMG_URL = getenv(
    "STREAM_IMG_URL",
    "LippsMusic/assets/Stream.jpeg",
)

SOUNCLOUD_IMG_URL = getenv(
    "SOUNCLOUD_IMG_URL",
    "LippsMusic/assets/Soundcloud.jpeg",
)

YOUTUBE_IMG_URL = getenv(
    "YOUTUBE_IMG_URL",
    "LippsMusic/assets/Youtube.jpeg",
)

SPOTIFY_ARTIST_IMG_URL = getenv(
    "SPOTIFY_ARTIST_IMG_URL",
    "LippsMusic/assets/SpotifyArtist.jpeg",
)

SPOTIFY_ALBUM_IMG_URL = getenv(
    "SPOTIFY_ALBUM_IMG_URL",
    "LippsMusic/assets/SpotifyAlbum.jpeg",
)

SPOTIFY_PLAYLIST_IMG_URL = getenv(
    "SPOTIFY_PLAYLIST_IMG_URL",
    "LippsMusic/assets/SpotifyPlaylist.jpeg",
)



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
