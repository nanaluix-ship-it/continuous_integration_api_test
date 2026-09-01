import requests


def get_echo_data():
    url = "https://postman-echo.com/get"

    response = requests.get(url, timeout=10)
    return response.json()
