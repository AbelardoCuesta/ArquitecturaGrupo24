import requests
import json
import time

url = "http://localhost:5000/salida"


ads = [] # this is where I am going to store the data

for i in range(0,100): 

    payload = {"identificacion": 146684655}
    try:
        response = requests.get(url, json=payload)
        status = response.status_code


        if (status==200):
            print("Microservicio salida disponible", status)
        else:
            print ("Microservicio salida disponible, pero backend no disponible, ", status)
            data = json.loads(response.text)
            ads.append(data)
    except requests.exceptions.RequestException:
        print ("Microservicio salida no disponible")

    data = json.loads(response.text)
    ads.append(data)
    time.sleep(3) 
# This is just me trying to be nice and not overloading their servers (or get myself 
# banned) by sending to many requests at once. time.sleep(3) introduces a #3-second 
# delay between requests.

with open("raw_ads.json", "w") as f:
    f.write(json.dumps(ads))
