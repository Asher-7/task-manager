import hashlib
from functools import partial

import pytest

from app import create_app
from app.database import db
from app.routes import auth

# Werkzeug defaults to scrypt, which is missing from Pythons built against
# LibreSSL (e.g. the macOS system Python). Fall back to PBKDF2 for tests only.
if not hasattr(hashlib, "scrypt"):
    auth.generate_password_hash = partial(auth.generate_password_hash, method="pbkdf2:sha256")


@pytest.fixture
def app():
    app = create_app({
        "TESTING": True,
        "SQLALCHEMY_DATABASE_URI": "sqlite:///:memory:",
    })
    yield app
    with app.app_context():
        db.session.remove()
        db.drop_all()


@pytest.fixture
def client(app):
    return app.test_client()


@pytest.fixture
def auth_client(client):
    """A test client that is registered and logged in as 'alice'."""
    res = client.post("/auth/register", json={
        "username": "alice",
        "email": "alice@example.com",
        "password": "secret",
    })
    assert res.status_code == 201
    return client
