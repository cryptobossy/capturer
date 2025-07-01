# Capturer Bot - Despliegue en PythonAnywhere

Este proyecto es un bot de Telegram con backend en Flask y base de datos gestionada con SQLAlchemy y Alembic.

## Requisitos

- Cuenta en [PythonAnywhere](https://www.pythonanywhere.com/)
- Python 3.11+ en PythonAnywhere
- Token de bot de Telegram y chat ID de administrador

## Pasos para desplegar

### 1. Sube tu código

Puedes subir tu código usando Git o cargando los archivos manualmente en el dashboard de PythonAnywhere.

### 2. Crea un entorno virtual

En la consola de PythonAnywhere:

```sh
python3.11 -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
```

### 3. Configura variables de entorno

Crea un archivo `.env` en el directorio raíz con el siguiente contenido (ajusta tus valores):

```
TELEGRAM_TOKEN=tu_token_de_telegram
ADMIN_CHAT_ID=tu_chat_id
DATABASE_URL=mysql+pymysql://usuario:contraseña@host/nombre_db
```

### 4. Configura la base de datos

Si usas MySQL de PythonAnywhere, crea la base de datos desde el dashboard.

Inicializa la base de datos y aplica migraciones:

```sh
export FLASK_APP=manage.py
flask db upgrade
```

### 5. Configura la aplicación web

En el dashboard de PythonAnywhere, ve a "Web" y crea una nueva app Flask.

- **Source code**: apunta al directorio de tu proyecto.
- **WSGI file**: edita el archivo WSGI para incluir tu app Flask, por ejemplo:

```python
import sys
path = '/home/tu_usuario/ruta/a/tu/proyecto'
if path not in sys.path:
    sys.path.insert(0, path)

from flask_app import app as application
```

### 6. Configura el webhook de Telegram

Ejecuta en la consola de PythonAnywhere:

```sh
python update_webhook.py
```
Introduce tu dominio de PythonAnywhere (ejemplo: `https://tu_usuario.pythonanywhere.com`).

### 7. Reinicia la web app

Desde el dashboard de PythonAnywhere, reinicia tu aplicación web.

---

## Pruebas

Puedes probar la conexión a Telegram accediendo a `/test-telegram` en tu dominio.

---

## Estructura del proyecto

- `flask_app.py`: punto de entrada principal
- `manage.py`: comandos y migraciones
- `app/`: código fuente principal
- `requirements.txt`: dependencias

---

## Notas

- Asegúrate de que tu archivo `.env` no esté en el repositorio público.
- Si cambias el dominio, recuerda actualizar el webhook.

---

¡Listo! Tu bot debería estar funcionando en PythonAnywhere.