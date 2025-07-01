from app.services.account import UserService
from app.utils.send_list import send_user_list
from app.config import Config
def amount():
    """
    Returns the amount of registered users.
    This function is a placeholder and should be replaced with actual logic to retrieve user count.
    """
    return f"Cantidad de usuarios registrados: {UserService.user_count()}"
def list_users():
    """
    Returns a list of registered users.
    """
    send_user_list(Config.ADMIN_CHAT_ID)
    return None