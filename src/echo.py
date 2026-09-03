"""Модуль для отправки HTTP-запросов к postman-echo."""
import requests


def get_echo_data():
    """Отправляет простой GET-запрос без параметров и возвращает JSON-ответ."""
    url = "https://postman-echo.com/get"
    response = requests.get(url, timeout=10)
    response.raise_for_status()
    return response.json()


def get_echo_with_params(params):
    """Отправляет GET-запрос с параметрами и возвращает JSON-ответ."""
    url = "https://postman-echo.com/get"
    response = requests.get(url, params=params, timeout=10)
    response.raise_for_status()
    return response.json()

def post_simple(payload):
    """Отправляет POST-запрос с JSON-параметрами и возвращает JSON-ответ."""
    url = "https://postman-echo.com/post"
    response = requests.post(url, json=payload, timeout=10)
    response.raise_for_status()
    return response.json()

def post_form_data(form_payload):
    """Отправляет POST-запрос с multipart/form-data и возвращает JSON-ответ."""
    url = "https://postman-echo.com/post"
    response = requests.post(url, data=form_payload, timeout=10)
    response.raise_for_status()
    return response.json()
