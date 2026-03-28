from main import UserManager
import pytest

# bài 1
# def test_get_weather():
#     assert get_weather(19) == "hot"



# bai 2
# def test_add():
#     assert add(2, 3) == 5
#     assert add(-1, 1) == 0
#     assert add(0, 0) == 0

# def test_divide():
#    with pytest.raises(ValueError,match="Cannot divide by zero"):
#        divide(10, 0)

# bai 3
@pytest.fixture
def user_manager():
    """Creates a fresh instance of UserManager before each test."""
    return UserManager()
    
def test_add_user(user_manager):
    assert user_manager.add_user("bob", "123") == True
    assert user_manager.get_user("bob") == "123"

def test_add_duplicate_user(user_manager):
    user_manager.add_user("bob", "123")
    with pytest.raises(ValueError):
        user_manager.add_user("bob", "456")