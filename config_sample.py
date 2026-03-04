# ⚡𝗛𝗘𝗠𝗔𝗡𝗧𝗛⚡ Mirror-Leech Bot Configuration File Template

# REQUIRED CONFIG
BOT_TOKEN = ""                          # Get this from @BotFather
OWNER_ID = 0                            # Your Telegram User ID
TELEGRAM_API = 0                        # Get this from https://my.telegram.org
TELEGRAM_HASH = ""                      # Get this from https://my.telegram.org
DATABASE_URL = ""                       # MongoDB Database URL

# OPTIONAL CONFIG
DEFAULT_LANG = "en"                     # Bot language (en, bn, etc.)
TG_PROXY = {}                           # Telegram Proxy
USER_SESSION_STRING = ""                # Pyrogram session string for premium features
CMD_SUFFIX = ""                         # Suffix to add to bot commands
AUTHORIZED_CHATS = ""                   # IDs of chats authorized to use the bot
SUDO_USERS = ""                         # IDs of users with sudo privileges
STATUS_LIMIT = 10                       # Max number of tasks to show in status
DEFAULT_UPLOAD = "rc"                   # Default upload destination (gd or rc)
STATUS_UPDATE_INTERVAL = 15             # Interval in seconds to update status messages
FILELION_API = ""                       # FileLion API key
STREAMWISH_API = ""                     # StreamWish API key
EXCLUDED_EXTENSIONS = ""                # Extensions to exclude from uploads
INCOMPLETE_TASK_NOTIFIER = False        # Notify if tasks were incomplete after restart
YT_DLP_OPTIONS = ""                     # Custom options for yt-dlp
USE_SERVICE_ACCOUNTS = False            # Use Google Service Accounts for GDrive
NAME_SWAP = ""                          # Swap names in files
FFMPEG_CMDS = {}                        # Custom FFmpeg commands
UPLOAD_PATHS = {}                       # Custom upload paths for Rclone

# Hyper Tg Downloader
HELPER_TOKENS = ""                      # Space separated helper bot tokens

# MegaAPI
MEGA_EMAIL = ""                         # Mega.nz email
MEGA_PASSWORD = ""                      # Mega.nz password

# Disable Options
DISABLE_TORRENTS = False
DISABLE_LEECH = False
DISABLE_BULK = False
DISABLE_MULTI = False
DISABLE_SEED = False
DISABLE_FF_MODE = False

# Telegraph
AUTHOR_NAME = "⚡𝗛𝗘𝗠𝗔𝗡𝗧𝗛⚡"
AUTHOR_URL = "https://t.me/ALONEKINGSTAR77"

# Task Limits (0 for no limit)
DIRECT_LIMIT = 0
MEGA_LIMIT = 0
TORRENT_LIMIT = 0
GD_DL_LIMIT = 0
RC_DL_LIMIT = 0
CLONE_LIMIT = 0
JD_LIMIT = 0
NZB_LIMIT = 0
YTDLP_LIMIT = 0
PLAYLIST_LIMIT = 0
LEECH_LIMIT = 0
EXTRACT_LIMIT = 0
ARCHIVE_LIMIT = 0
STORAGE_LIMIT = 0

# Insta video downloader api
INSTADL_API = ""

# Nzb search
HYDRA_IP = ""
HYDRA_API_KEY = ""

# Media Search Template
IMDB_TEMPLATE = """<b>Title: </b> {title} [{year}]
<b>Also Known As:</b> {aka}
<b>Rating ⭐️:</b> <i>{rating}</i>
<b>Release Info: </b> <a href="{url_releaseinfo}">{release_date}</a>
<b>Genre: </b>{genres}
<b>IMDb URL:</b> {url}
<b>Language: </b>{languages}
<b>Country of Origin : </b> {countries}

<b>Story Line: </b><code>{plot}</code>

<a href="{url_cast}">Read More ...</a>"""

# Task Tools
FORCE_SUB_IDS = ""
MEDIA_STORE = True
DELETE_LINKS = False
CLEAN_LOG_MSG = False

# Limiters
BOT_MAX_TASKS = 0
USER_MAX_TASKS = 0
USER_TIME_INTERVAL = 0
VERIFY_TIMEOUT = 0
LOGIN_PASS = ""

# Bot Settings
BOT_PM = False
SET_COMMANDS = True
TIMEZONE = "Asia/Kolkata"

# GDrive Tools
GDRIVE_ID = ""
GD_DESP = "Uploaded with ⚡𝗛𝗘𝗠𝗔𝗡𝗧𝗛⚡ Bot"
IS_TEAM_DRIVE = False
STOP_DUPLICATE = False
INDEX_URL = ""

# YT Tools
YT_DESP = "Uploaded to YouTube by ⚡𝗛𝗘𝗠𝗔𝗡𝗧𝗛⚡ bot"
YT_TAGS = ["telegram", "bot", "youtube"]
YT_CATEGORY_ID = 22
YT_PRIVACY_STATUS = "unlisted"

# Rclone
RCLONE_PATH = ""
RCLONE_FLAGS = ""
RCLONE_SERVE_URL = ""
SHOW_CLOUD_LINK = True
RCLONE_SERVE_PORT = 0
RCLONE_SERVE_USER = ""
RCLONE_SERVE_PASS = ""

# JDownloader
JD_EMAIL = ""
JD_PASS = ""

# Sabnzbd
USENET_SERVERS = []

# Update
UPSTREAM_REPO = ""
UPSTREAM_BRANCH = "master"
UPDATE_PKGS = True

# Leech
LEECH_SPLIT_SIZE = 0
AS_DOCUMENT = False
EQUAL_SPLITS = False
MEDIA_GROUP = False
USER_TRANSMISSION = True
HYBRID_LEECH = True
LEECH_PREFIX = ""
LEECH_SUFFIX = ""
LEECH_FONT = ""
LEECH_CAPTION = ""
THUMBNAIL_LAYOUT = ""

# Log Channels
LEECH_DUMP_CHAT = ""
LINKS_LOG_ID = ""
MIRROR_LOG_ID = ""

# qBittorrent/Aria2c
TORRENT_TIMEOUT = 0
BASE_URL = ""
BASE_URL_PORT = 0
WEB_PINCODE = True

# Queueing system
QUEUE_ALL = 0
QUEUE_DOWNLOAD = 0
QUEUE_UPLOAD = 0

# RSS
RSS_DELAY = 600
RSS_CHAT = ""
RSS_SIZE_LIMIT = 0

# Torrent Search
SEARCH_API_LINK = ""
SEARCH_LIMIT = 0
SEARCH_PLUGINS = [
    "https://raw.githubusercontent.com/qbittorrent/search-plugins/master/nova3/engines/piratebay.py",
    "https://raw.githubusercontent.com/qbittorrent/search-plugins/master/nova3/engines/limetorrents.py",
    "https://raw.githubusercontent.com/qbittorrent/search-plugins/master/nova3/engines/torlock.py",
    "https://raw.githubusercontent.com/qbittorrent/search-plugins/master/nova3/engines/torrentscsv.py",
    "https://raw.githubusercontent.com/qbittorrent/search-plugins/master/nova3/engines/eztv.py",
    "https://raw.githubusercontent.com/qbittorrent/search-plugins/master/nova3/engines/torrentproject.py",
    "https://raw.githubusercontent.com/MaurizioRicci/qBittorrent_search_engines/master/kickass_torrent.py",
    "https://raw.githubusercontent.com/MaurizioRicci/qBittorrent_search_engines/master/yts_am.py",
    "https://raw.githubusercontent.com/MadeOfMagicAndWires/qBit-plugins/master/engines/linuxtracker.py",
    "https://raw.githubusercontent.com/MadeOfMagicAndWires/qBit-plugins/master/engines/nyaasi.py",
    "https://raw.githubusercontent.com/LightDestory/qBittorrent-Search-Plugins/master/src/engines/ettv.py",
    "https://raw.githubusercontent.com/LightDestory/qBittorrent-Search-Plugins/master/src/engines/glotorrents.py",
    "https://raw.githubusercontent.com/LightDestory/qBittorrent-Search-Plugins/master/src/engines/thepiratebay.py",
    "https://raw.githubusercontent.com/v1k45/1337x-qBittorrent-search-plugin/master/leetx.py",
    "https://raw.githubusercontent.com/nindogo/qbtSearchScripts/master/magnetdl.py",
    "https://raw.githubusercontent.com/msagca/qbittorrent_plugins/main/uniondht.py",
    "https://raw.githubusercontent.com/khensolomon/leyts/master/yts.py",
]
