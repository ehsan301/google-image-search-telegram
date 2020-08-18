import os

BOT_NAME = os.environ.get("BOT_NAME", "seanerbot")
CSE_KEY = os.environ.get("CSE_KEY", "SOingHFtVNwfQi6MwwvEfqjg")
CSE_CX = os.environ.get("CSE_CX", "790451702465-e637mpic03sok6qa2ora64r43n8k5c64.apps.googleusercontent.com")
API_TOKEN = os.environ.get("API_TOKEN", "1371564155:AAFeM_g5fiQPOpT4f1N7PLTkXdCJra3-kk4")
WEBHOOK_URL = os.environ.get("WEBHOOK_URL", "https://seanerbot.heroku.com/")
NGINX_SUBPATH = os.environ.get("NGINX_SUBPATH", "")
BATCH = int(os.environ.get("BATCH", 15))
POLLING = bool(os.environ.get("POLLING", False))
