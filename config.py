# Don't Edit

import os

from dotenv import load_dotenv
load_dotenv()


# Mandatory variables for the bot to start
API_ID = int(os.getenv("API_ID", "26181458"))
API_HASH = os.environ.get("API_HASH", "09c734fa0c97721650b5dc0cdbd679d7")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "6055102443:AAH_JHCZ0qT0zSRh4D9H5tGSHEMSHfPboo4")
ADMINS = [int(i.strip()) for i in os.environ.get("ADMINS").split("Owner Id")] if os.environ.get("ADMINS") else []
ADMIN = ADMINS
DATABASE_NAME = os.environ.get("DATABASE_NAME", "GMDB")
DATABASE_URL = os.getenv("DATABASE_URL", "mongodb+srv://srikanthnayak:srikanthnayak@cluster0.bdl1rjd.mongodb.net/?retryWrites=true&w=majority") 
OWNER_ID =  int(os.environ.get("OWNER_ID", "5856362162")) 
ADMINS.append(OWNER_ID) if OWNER_ID not in ADMINS else []
ADMINS.append(Id Owned Id)
#  Optionnal variables
LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1001982224461")) 
UPDATE_CHANNEL = os.environ.get("UPDATE_CHANNEL", "GeethaMovies") # For Force Subscription
BROADCAST_AS_COPY = os.environ.get('BROADCAST_AS_COPY', "True") # true if forward should be avoided
WELCOME_IMAGE = os.environ.get("WELCOME_IMAGE", '') # image when someone hit /start # image when someone hit /start
LINK_BYPASS = "False"
