import requests
from app.config import Config
def send_telegram_message(chat_id, text):
    try:
        url = f"https://api.telegram.org/bot{Config.__TELEGRAM_BOT_TOKEN__}/sendMessage"
        payload = {'chat_id': chat_id, 'text': text, 'parse_mode': 'HTML'}
        response = requests.post(url, json=payload, timeout=10)

        # Registro detallado (verás esto en los logs de PythonAnywhere)
        print(f"""
        ⚡️ Intento de envío a Telegram:
        - URL: {url}
        - Chat ID: {chat_id}
        - Texto: {text[:50]}...
        - Status: {response.status_code}
        - Respuesta: {response.text}
        """)

        return response.json()
    except Exception as e:
        print(f"🚨 Error en send_telegram_message: {str(e)}")
        return None