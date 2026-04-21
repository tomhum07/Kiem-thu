# bài 1 
# def get_weather(temp):
#     if temp > 20:
#         return "hot"
#     else:
#         return "cold"

# bai 2
# def add(a, b):
#     return a + b


# def divide(a, b):
#     if b == 0:
#         raise ValueError("Cannot divide by zero")
#     return a / b

# bai 3
# class UserManager:
#     def __init__(self):
#         self.users = {}

#     def add_user(self, username, password):
#         if username in self.users:
#             raise ValueError("User already exists")
#         self.users[username] = password
#         return True
    
#     def get_user(self, username):
#         return self.users.get(username)


# bài 4
# def is_prime(n):
#     if n <= 2:
#         return False
#     for i in range(2, int(n**0.5) + 1):
#         if n % i == 0:
#             return False
#     return True 


# bài 5
import requests
def get_weather(city):
    response = requests.get(f"http://api.weather.com/v1/{city}")
    if response.status_code == 200:
        return response.json()
    else:
        raise ValueError("Could not fetch weather data")