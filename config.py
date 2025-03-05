from os import environ

from dotenv import load_dotenv

load_dotenv()

JWT_KEY = environ["JWT_KEY"]

GOOGLE_CLIENT_ID = environ["GOOGLE_CLIENT_ID"]
GOOGLE_CLIENT_SECRET = environ["GOOGLE_CLIENT_SECRET"]

FRONT_END_GOOGLE_LOGIN_URL = environ.get("FRONT_END_GOOGLE_LOGIN_URL")

MONGO_USER = environ["MONGO_USER"]
MONGO_PASS = environ["MONGO_PASS"]
MONGO_URI = environ["MONGO_URI"]
MONGO_APP = environ["MONGO_APP"]
MONGO_DB = environ["MONGO_DB"]
