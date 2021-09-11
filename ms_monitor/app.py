import requests
import json
import time
import logging


logger = logging.getLogger("Basic Logger")
logger.setLevel(logging.INFO)


stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.INFO)
logger.addHandler(stream_handler)


file_handler = logging.FileHandler("error.log")
file_handler.setLevel(logging.ERROR)
logger.addHandler(file_handler)


url = "http://localhost:5000/salida"


ads = [] # this is where I am going to store the data

for i in range(0,100): 

    payload = {"identificacion": 146684655}
    try:
        response = requests.get(url, json=payload)
        status = response.status_code


        if (status==200):
            #with open("raw_ads.json", "a") as f:
             #   f.write(json.dumps("Microservicio salida disponible " + str(status) + '\\n'))
            print("Microservicio salida disponible " + str(status))
            logger.critical("Microservicio salida disponible "+ str(status))
        else:
            print ("Microservicio salida disponible, pero backend no disponible, "+ str(status))
            logger.critical("Microservicio salida disponible, pero backend no disponible, "+ str(status))
            data = json.loads(response.text)
            ads.append(data)
    except requests.exceptions.RequestException:
        print ("Microservicio salida no disponible")
        logger.critical("Microservicio salida no disponible")

    data = json.loads(response.text)
    ads.append(data)
    time.sleep(3) 
# This is just me trying to be nice and not overloading their servers (or get myself 
# banned) by sending to many requests at once. time.sleep(3) introduces a #3-second 
# delay between requests.

with open("raw_ads.json", "w") as f:
    f.write(json.dumps(ads))
