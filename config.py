import re, os

id_pattern = re.compile(r'^.\d+$') 

API_ID = os.environ.get("API_ID", "1234567")
API_HASH = os.environ.get("API_HASH", "12345e234e12467fjra5f18bie1dd7")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")

CHANNEL = os.environ.get("CHANNEL", "CrazyXBots") # username without '@'
BOT_USERNAME = os.environ.get("BOT_USERNAME","") # username without '@'
SUPPORT_GROUP = os.environ.get("SUPPORT_GROUP","CrazyXBots_Support") # username without '@'
UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL","CrazyXBots") # username without '@'
OWNER_USERNAME = os.environ.get("OWNER_USERNAME","KicchaFanMahi")
STRING = os.environ.get("STRING", "")

DB_NAME = os.environ.get("DB_NAME","CrazyXBots")     
DB_URL = os.environ.get("DB_URL","")

FLOOD = int(os.environ.get("FLOOD", "90"))
LAZY_PIC = os.environ.get("LAZY_PIC", "https://graph.org/file/d132594c0967e45270962.jpg")
ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '').split()]
PORT = os.environ.get('PORT', '8080')
LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-100"))

