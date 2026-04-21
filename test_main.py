from main import get_weather
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
# @pytest.fixture
# def user_manager():
#     """Creates a fresh instance of UserManager before each test."""
#     return UserManager()
    
# def test_add_user(user_manager):
#     assert user_manager.add_user("bob", "123") == True
#     assert user_manager.get_user("bob") == "123"

# def test_add_duplicate_user(user_manager):
#     user_manager.add_user("bob", "123")
#     with pytest.raises(ValueError):
#         user_manager.add_user("bob", "456")

# bài 4
# @pytest.mark.parametrize("num, expected", [
#     (1, False),
#     (2, True),
#     (3, True),
#     (4, False),
#     (5, True),
#     (10, False),
#     (13, True) 
# ])
# def test_is_prime(num, expected):
#     assert is_prime(num) == expected

# bài 5
def test_get_weather(mocker):

    #Mock requests.get
    mock_get = mocker.patch('main.requests.get')
    
    #set return value
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {"temperature": 25, "condition": "sunny"}
    
    #call the function
    result = get_weather("Dubai")

    #Asserttions
    assert result == {"temperature": 25, "condition": "sunny"} 
    mock_get.assert_called_once_with(f"http://api.weather.com/v1/Dubai")


