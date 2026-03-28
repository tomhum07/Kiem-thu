import pytest
from main import Database

@pytest.fixture
def db():
    """Creates a fresh instance of Database before each test."""
    database = Database()
    yield database
    database.data.clear() 

def test_add_user(db):
    db.add_user("1", "Alice")
    assert db.get_user("1") == "Alice"

def test_add_duplicate_user(db):
    db.add_user("1", "Alice")
    with pytest.raises(ValueError):
        db.add_user("1", "Bob")

def test_delete_user(db):
    db.add_user("2", "bob")
    db.delete_user("2")
    assert db.get_user("2") is None 