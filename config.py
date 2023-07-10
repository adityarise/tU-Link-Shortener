# Don't Edit

import os

from dotenv import load_dotenv
load_dotenv()


# Mandatory variables for the bot to start
API_ID = int(os.getenv("API_ID", "28900444"))
API_HASH = os.environ.get("API_HASH", "7343be63958388e1d88c2961efe5a9e6")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "6347076067:AAEjaRzOJXc9pCiRbPGkgUH-cFHNm6ND-iU")
ADMINS = [int(i.strip()) for i in os.environ.get("ADMINS").split("Owner Id")] if os.environ.get("ADMINS") else []
ADMIN = ADMINS
DATABASE_NAME = os.environ.get("DATABASE_NAME", "FORTU")
DATABASE_URL = os.getenv("DATABASE_URL", "mongodb+srv://aditya3:0yzxfmfbEuQjL1fz@cluster0.uxteiys.mongodb.net/?retryWrites=true&w=majority") 
OWNER_ID =  int(os.environ.get("OWNER_ID", "5397893493")) 
ADMINS.append(OWNER_ID) if OWNER_ID not in ADMINS else []
ADMINS.append(5397893493)
#  Optionnal variables
LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "--1001956473590 For Force Subscription
BROADCAST_AS_COPY = os.environ.get('BROADCAST_AS_COPY', "True") # true if forward should be avoided
WELCOME_IMAGE = os.environ.get("WELCOME_IMAGE", '') # image when someone hit /start # image when someone hit /start
LINK_BYPASS = "False"
