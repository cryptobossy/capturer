from app.services.account import UserService
from app.utils.message import send_telegram_message

def send_user_list(chat_id):
    """
    Envía un mensaje por cada usuario, mostrando cada dato del diccionario en una línea.
    """
    users = UserService.get_user_list()
    if not users:
        send_telegram_message(chat_id, "No hay usuarios registrados.")
        return

    for user in users:
        # user es un UserBase, lo convertimos a dict
        user_dict = user.model_dump()
        lines = [f"<b>{k}:</b> {v}" for k, v in user_dict.items() if v is not None]
        message = "\n".join(lines)
        send_telegram_message(chat_id, message)