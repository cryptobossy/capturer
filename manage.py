from flask import Flask
from flask_migrate import Migrate
from app import Config
from app.sql import db
from app.database.account import UserDB

import os

def create_app(testing=False):
    app = Flask(__name__)
    if testing:
        app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('TEST_DATABASE_URI', 'sqlite:///test.db')
        app.config["TESTING"] = True
    else:
        app.config["SQLALCHEMY_DATABASE_URI"] = Config.SQLALCHEMY_DATABASE_URI
    db.init_app(app)
    return app

# Detecta si se debe usar la base de datos de test
testing = os.environ.get("USE_TEST_DB", "0") == "1"
app = create_app(testing=testing)
migrate = Migrate(app, db)

if __name__ == "__main__":
    app.run()