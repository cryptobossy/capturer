import os
from dotenv import load_dotenv
from pathlib import Path
from app.services.account import UserService
from utils.send_list import send_user_list
# Load environment variables from .env file
Path(".env").expanduser().resolve()
load_dotenv()
def dot(data:int):
    return "."
class Config:
    __TELEGRAM_BOT_TOKEN__ = os.getenv("TELEGRAM_TOKEN", "your_telegram_token_here")
    TELEGRAM_API_URL = f"https://api.telegram.org/bot{__TELEGRAM_BOT_TOKEN__}"
    ADMIN_CHAT_ID = int(os.getenv("OWNER_CHAT_ID", 0))
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "sqlite:///test.db")
    TEST_DATABASE_URI = os.getenv("TEST_DATABASE_URL", "sqlite:///test.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_BINDS = {
        "default": SQLALCHEMY_DATABASE_URI}
    DEVELOPMENT = bool(os.getenv("DEVELOPMENT",True))
    ADMIN_COMMANDS = {
        "/greet" : f"Saludos, administrador{dot}",
        "/amount": f"Cantidad de usuarios registrados: {UserService.user_count()}{dot}",
        "/list": f"Lista de usuarios registrados {send_user_list(ADMIN_CHAT_ID)}",
    }
    ALLOWED_USERS = [ADMIN_CHAT_ID]