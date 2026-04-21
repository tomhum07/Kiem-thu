# import pytest
# from main import Database

# @pytest.fixturepy
# def db():
#     """Creates a fresh instance of Database before each test."""
#     database = Database()
#     yield database
#     database.data.clear() 

# def test_add_user(db):
#     db.add_user("1", "Alice")
#     assert db.get_user("1") == "Alice"

# def test_add_duplicate_user(db):
#     db.add_user("1", "Alice")
#     with pytest.raises(ValueError):
#         db.add_user("1", "Bob")

# def test_delete_user(db):
#     db.add_user("2", "bob")
#     db.delete_user("2")
#     assert db.get_user("2") is None 

# bài 6
from db import save_user

def test_save_user(mocker):
    mock_conn = mocker.patch('sqlite3.connect')
    mock_cursor = mock_conn.return_value.cursor.return_value

    save_user("Alice", 30)

    mock_conn.assert_called_once_with('users.db')
    mock_cursor.execute.assert_called_once_with(" INSERT INTO users (name, age) VALUES (?, ?)", ("Alice", 30))