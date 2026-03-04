# ruff: noqa: E402

from uvloop import install
install()

import asyncio
from os import getcwd, cpu_count, path as ospath
from time import time
from logging import (
    ERROR,
    INFO,
    WARNING,
    FileHandler,
    StreamHandler,
    basicConfig,
    getLogger,
)

from apscheduler.schedulers.asyncio import AsyncIOScheduler
from .core.config_manager import BinConfig
from .sabnzbdapi import SabnzbdClient

# Suppress noisy logs
getLogger("requests").setLevel(WARNING)
getLogger("urllib3").setLevel(WARNING)
getLogger("pyrogram").setLevel(ERROR)
getLogger("aiohttp").setLevel(ERROR)
getLogger("apscheduler").setLevel(ERROR)
getLogger("httpx").setLevel(WARNING)
getLogger("pymongo").setLevel(WARNING)

bot_start_time = time()

# We will use the loop from asyncio.run() in main.py
bot_loop = None

basicConfig(
    format="[%(asctime)s] [%(levelname)s] - %(message)s",
    datefmt="%d-%b-%y %I:%M:%S %p",
    handlers=[FileHandler("log.txt"), StreamHandler()],
    level=INFO,
)

LOGGER = getLogger(__name__)

cpu_no = cpu_count() or 4
threads = max(1, cpu_no)

bot_cache = {}
DOWNLOAD_DIR = ospath.join(getcwd(), "downloads/")
intervals = {"status": {}, "qb": "", "jd": "", "nzb": "", "stopAll": False}
qb_torrents = {}
jd_downloads = {}
nzb_jobs = {}
user_data = {}
aria2_options = {}
qbit_options = {}
nzb_options = {}
queued_dl = {}
queued_up = {}
status_dict = {}
task_dict = {}
rss_dict = {}
shortener_dict = {}

auth_chats = {}
excluded_extensions = ["aria2", "!qB"]
drives_names = []
drives_ids = []
index_urls = []
sudo_users = []
non_queued_dl = set()
non_queued_up = set()
multi_tags = set()

task_dict_lock = asyncio.Lock()
queue_dict_lock = asyncio.Lock()
qb_listener_lock = asyncio.Lock()
nzb_listener_lock = asyncio.Lock()
jd_listener_lock = asyncio.Lock()
cpu_eater_lock = asyncio.Lock()
same_directory_lock = asyncio.Lock()

sabnzbd_client = SabnzbdClient(
    host="http://localhost",
    api_key="admin",
    port="8070",
)

scheduler = AsyncIOScheduler()

async def start_qbittorrent():
    try:
        cmd = [BinConfig.QBIT_NAME, "-d", f"--profile={getcwd()}"]
        process = await asyncio.create_subprocess_exec(*cmd)
        await process.wait()
        LOGGER.info("qBittorrent started.")
    except Exception as e:
        LOGGER.error(f"Failed to start qBittorrent: {e}")
