import requests
import json
import time

url = "http://localhost:5000/echo"


ads = [] # this is where I am going to store the data

for i in range(0,100): 

    payload = {"cliente": "monitor1"}  
    try:
        response = requests.get(url, json=payload)
        status = response.status_code
        print ("Microservicio disponible, ", status)
        data = json.loads(response.text)
        ads.append(data)
    except requests.exceptions.RequestException:
        print ("Microservicio no disponible")

    data = json.loads(response.text)
    ads.append(data)
    time.sleep(3) 
# This is just me trying to be nice and not overloading their servers (or get myself 
# banned) by sending to many requests at once. time.sleep(3) introduces a #3-second 
# delay between requests.

with open("raw_ads.json", "w") as f:
    f.write(json.dumps(ads))
