# Copyright (c) 2023 EDM115
import os


class Config:
    APP_ID = int(os.environ.get("APP_ID", "20263428"))
    API_HASH = os.environ.get("API_HASH", "f9dc42564f6e6eb9920912b09f729e3f")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6222983478:AAHcISRe4SnSFWlxtinm4m88nuKUhHRkbKo")
    LOGS_CHANNEL = int(os.environ.get("LOGS_CHANNEL",-1001973804769))
    MONGODB_URL = os.environ.get("MONGODB_URL","mongodb+srv://Luciferbin:9339119160@cluster0.kmbiojj.mongodb.net/?retryWrites=true&w=majority")
    BOT_OWNER = int(os.environ.get("BOT_OWNER", "25004026"))
    SESSION_STRING = os.environ.get("SESSION_STRING") if os.environ.get("SESSION_STRING") else None
    DOWNLOAD_LOCATION = f"{os.path.dirname(__file__)}/Downloaded"
    THUMB_LOCATION = f"{os.path.dirname(__file__)}/Thumbnails"
    TG_MAX_SIZE = 2097152000
    TG_PREMIUM_SIZE = TG_MAX_SIZE * 2
    # Default chunk size (0.005 MB → 1024*6) Increase if you need faster downloads
    CHUNK_SIZE = 1024 * 1024 * 10  # 10 MB
    BOT_THUMB = f"{os.path.dirname(__file__)}/bot_thumb.jpg"
    MAX_CONCURRENT_TASKS = 50
    MAX_TASK_DURATION_EXTRACT = 45 * 60  # 45 minutes (in seconds)
    MAX_TASK_DURATION_MERGE = 90 * 60  # 1 hour 30 minutes (in seconds)
