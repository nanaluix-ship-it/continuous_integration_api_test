import requests


def get_echo_data():
    url = "https://postman-echo.com/get"
    response = requests.get(url, timeout=10)
    response.raise_for_status()
    return response.json()


def get_echo_with_params(params):
    url = "https://postman-echo.com/get"
    response = requests.get(url, params=params, timeout=10)
    response.raise_for_status()
    return response.json()

def post_simple(payload):
    url = "https://postman-echo.com/post"
    response = requests.post(url, json=payload, timeout=10)
    response.raise_for_status()
    return response.json()

def post_form_data(form_payload):
    url = "https://postman-echo.com/post"
    response = requests.post(url, data=form_payload, timeout=10)
    response.raise_for_status()
    return response.json()