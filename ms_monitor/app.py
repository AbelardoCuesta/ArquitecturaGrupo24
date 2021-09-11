import requests
import json
import time
from .logger import log
from flask import Flask

url = "http://localhost:5000/salida"
ads = []  # this is where I am going to store the data
response = None
app = Flask("Flask Example Server")


for i in range(0, 100):

    payload = {"identificacion": 146684655}
    try:
        response = requests.get(url, json=payload)
        status = response.status_code

        if status == 200:
            log.info("Microservicio salida disponible.", **response)
        else:
            log.critical("Microservicio salida disponible, pero backend no disponible.", **response)
            data = json.loads(response.text)
            ads.append(data)
    except requests.exceptions.RequestException:
        log.critical("Microservicio salida no disponible")

    if response is not None:
        data = json.loads(response.text)
        ads.append(data)
        time.sleep(3)

