import os

from os import environ

API_ID = int(os.environ.get('API_ID', ''))
API_HASH = os.environ.get("API_HASH", "")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "")

PASS_DB = int(os.environ.get("PASS_DB", "721"))

OWNER = int(os.environ.get("OWNER", 5997896353))

LOG_CHANNEL = int(environ.get('LOG_CHANNEL', '-1002063321661'))

try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "5997896353").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")
ADMINS.append(OWNER)


