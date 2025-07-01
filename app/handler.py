import json
from .config import Config
from app.utils.message import send_telegram_message

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
        if str(text).startswith('/') and str(text) in Config.ADMIN_COMMANDS.keys():
            responses = Config.ADMIN_COMMANDS
            send_telegram_message(chat_id, responses[text])
        elif not str(text).startswith('/'):
            send_telegram_message(chat_id, f"No se que es {text}, no puedo ayudarte con eso")
        else:
            # Aquí puedes agregar más lógica para otros comandos
            print(f"Mensaje recibido de {chat_id}: {text}")
            send_telegram_message(chat_id, f"Comando no reconocido: {text}")