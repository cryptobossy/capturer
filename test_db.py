from app.sql import db
from manage import create_app
from sqlalchemy import text

def test_db_connection():
    app = create_app(testing=False)
    with app.app_context():
        try:
            # Imprime la información de la base de datos
            print("Conectando a la base de datos:", app.config.get("SQLALCHEMY_DATABASE_URI"))
            # Ejecuta una consulta simple para verificar la conexión
            db.session.execute(text("SELECT 1"))
            print("Conexión exitosa a la base de datos.")
        except Exception as e:
            print("Error de conexión a la base de datos:", e)
            assert False, f"Error de conexión: {e}"

if __name__ == "__main__":
    test_db_connection()