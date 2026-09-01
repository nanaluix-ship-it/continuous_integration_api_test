import requests
from pprint import pprint

url = "https://postman-echo.com/get"

response = requests.get(url)
data = response.json()

pprint(data)