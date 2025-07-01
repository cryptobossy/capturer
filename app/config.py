import os
from dotenv import load_dotenv
from pathlib import Path

# Load environment variables from .env file
dotenv_path = Path(__file__).parent / ".env"
load_dotenv(dotenv_path)

class Config:
    __TELEGRAM_BOT_TOKEN__ = os.getenv("TELEGRAM_TOKEN", "your_telegram_token_here")
    TELEGRAM_API_URL = f"https://api.telegram.org/bot{__TELEGRAM_BOT_TOKEN__}"
    ADMIN_CHAT_ID = int(os.getenv("ADMIN_CHAT_ID", 0))
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "sqlite:///test.db")
    TEST_DATABASE_URI = os.getenv("TEST_DATABASE_URL", "sqlite:///test.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_BINDS = {
        "default": SQLALCHEMY_DATABASE_URI}
    DEVELOPMENT = bool(os.getenv("DEVELOPMENT", True))
    ADMIN_COMMANDS = {
        "/greet": lambda: "Saludos, administrador",
        "/amount": lambda: __import__('app.chat', fromlist=['amount']).amount(),
        "/list": lambda: __import__('app.chat', fromlist=['list_users']).list_users()
    }
    ALLOWED_USERS = [ADMIN_CHAT_ID]