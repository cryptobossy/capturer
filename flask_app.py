from flask import Flask, request, jsonify
from app.utils.message import send_telegram_message
from app.config import Config
from app.handler import Handlers
from app.models import UserBase
from app.services.account import UserService
from app.sql import db
app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)
@app.route('/')
def home():
    return "Bot de Telegram funcionando!"

@app.route('/webhook', methods=['POST'])
def telegram_webhook():
    try:
        data = request.json
        print("Datos recibidos:", data)  # Para depuración

        # Manejar diferentes tipos de actualizaciones
        if data is not None and 'message' in data:
            message = data['message']
            update_type = 'message'
        else:
            print("Tipo de update no manejado:", data.keys() if data else "data is None")
            return jsonify(success=True)

        # Verificar si es un mensaje con chat
        if 'chat' not in message:
            print(f"Update de tipo {update_type} no tiene chat:", message)
            return jsonify(success=True)

        chat_id = message['chat']['id']
        text = message.get('text', '').strip()

        # Solo procesar si es un mensaje de texto
        if not text:
            return jsonify(success=True)

        # Verificar si es el administrador
        if chat_id not in Config.ALLOWED_USERS:
            print(f"Usuario no autorizado: {chat_id}")
            send_telegram_message(Config.ADMIN_CHAT_ID, f"⚠️ Usuario no autorizado: {chat_id}\nMensaje: {text}")
            send_telegram_message(chat_id, "⚠️ No estás autorizado")
            return jsonify(success=True)

        Handlers.handle_text(text, chat_id)
        return jsonify(success=True)

    except Exception as e:
        # Registra el error completo
        import traceback
        error_trace = traceback.format_exc()
        print(f"🔥 ERROR CRÍTICO: {str(e)}\n{error_trace}")

        # Intenta notificar al admin vía Telegram
        send_telegram_message(Config.ADMIN_CHAT_ID, f"☠️ Error en webhook: {str(e)}")

        return jsonify(success=False, error=str(e)), 500

@app.route('/check', methods=['POST'])
def receive_email():
    """Endpoint para recibir datos de usuarios y enviar notificación a Telegram."""
    if not request.is_json:
        return jsonify(success=False, error="Formato de solicitud no válido. Se esperaba JSON."), 400
    data = request.get_json()
    if not data:
        return jsonify(success=False, error="No se recibieron datos."), 400

    try:
        # Valida y normaliza los datos usando el modelo Pydantic UserBase
        user = UserBase.model_validate(data)
    except Exception as e:
        return jsonify(success=False, error=str(e)), 400
    UserService.create_user(user)
    # Guardar email y notificar
    send_telegram_message(Config.ADMIN_CHAT_ID, f"📬 Nuevo usuario registrado:\n{user.model_dump_json(indent=2)}")

    return jsonify(success=True)

@app.route('/test-telegram')
def test_telegram():
    test_msg = "🔍 Prueba de conexión con Telegram"
    result = send_telegram_message(Config.ADMIN_CHAT_ID, test_msg)
    return jsonify(success=bool(result), response=result)

if __name__ == '__main__':
    app.run(debug=True)