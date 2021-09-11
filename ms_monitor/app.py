import requests
import json
import time
from .logger import log
from flask import Flask

url = "http://localhost:5002/salida"
ads = []  # this is where I am going to store the data
response = None
app = Flask("Flask Example Server")


for i in range(0, 100):

    payload = {"identificacion": 146684655}
    try:
        response = requests.get(url, json=payload)
        status = response.status_code

        if status == 200:
            data = json.loads(response.text)
            log.info("Microservicio salida disponible.", **data)
        else:

            log.critical("Microservicio salida disponible, pero backend no disponible.")
    except requests.exceptions.RequestException:
        log.critical("Microservicio salida no disponible")


    time.sleep(3)
    i=i+1
