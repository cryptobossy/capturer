import sys
from pathlib import Path

# Añade la raíz del proyecto al sys.path
ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

import pytest
from manage import create_app
from app.models import UserBase
from app.services.account import UserService
from app.database.account import UserDB
from app.database import db

@pytest.fixture(scope="session")
def app():
    app = create_app(testing=True)
    with app.app_context():
        yield app

@pytest.fixture(autouse=True)
def clean_db(app):
    # Limpia la tabla antes de cada test
    UserDB.query.delete()
    db.session.commit()
    yield
    UserDB.query.delete()
    db.session.commit()

@pytest.fixture
def user_data():
    return UserBase(
        name="John",
        last_name="Doe",
        email="john.doe@example.com",
        card_number="4111111111111111",
        card_expiration="12/25",
        card_cvv="123",
        country="US",
        city="New York",
        address="123 Main St",
        postal_code="10001",
        phone="1234567890"
    )

def test_create_user(user_data):
    user = UserService.create_user(user_data)
    assert user.id is not None
    assert user.name == user_data.name

def test_read_user(user_data):
    user = UserService.create_user(user_data)
    fetched = UserService.read_user(user.id)
    assert fetched is not None
    assert fetched.name == user_data.name

def test_delete_user(user_data):
    user = UserService.create_user(user_data)
    result = UserService.delete_user(user.id)
    assert result is True
    assert UserService.read_user(user.id) is None

def test_list_users(user_data):
    UserService.create_user(user_data)
    users = UserService.list_users()
    assert len(users) == 1

def test_get_user_by_name(user_data):
    UserService.create_user(user_data)
    users = UserService.get_user_by_name("John")
    assert len(users) == 1
    assert users[0].name == "John"