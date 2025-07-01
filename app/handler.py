import json
from .config import Config
from app.utils.message import send_telegram_message
from app.utils.send_list import send_user_list
from app.services.account import UserService
class Handlers:
    function_dict = {
        "test": send_telegram_message,
    }
    @staticmethod
    def handle_text(text, chat_id:int):
        """
        Maneja el texto recibido del usuario.
        Aquí puedes agregar la lógica para procesar diferentes comandos o mensajes.
        """
        if text == "/start":
            send_telegram_message(chat_id, "Hola, soy el bot de captura de datos. ¿En qué puedo ayudarte?")
        
        elif text == "/amount":
            send_telegram_message(chat_id, f"Cantidad de usuarios registrados: {UserService.user_count()}")
        elif text == "/list":
            send_user_list(chat_id)
        elif text == "/help":
            help_message = (
                "Comandos disponibles:\n"
                "/start - Iniciar el bot\n"
                "/amount - Mostrar la cantidad de usuarios registrados\n"
                "/list - Listar todos los usuarios registrados\n"
                "/help - Mostrar este mensaje de ayuda"
            )
            send_telegram_message(chat_id, help_message)
        elif str(text).startswith("/"):
            # Aquí puedes agregar más lógica para otros comandos
            print(f"Mensaje recibido de {chat_id}: {text}")
            send_telegram_message(chat_id, f"Comando no reconocido: {text}")
        else:
            send_telegram_message(chat_id, f"No se que es {text}, no puedo ayudarte con eso")
