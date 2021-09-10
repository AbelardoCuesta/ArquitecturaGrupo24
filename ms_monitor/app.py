import requests
import json
import time

url = "http://localhost:5000/echo"


ads = [] # this is where I am going to store the data

for i in range(0,5): # This is the for-loop for constructing the post-requests 
# (yes, this is weird. Normally you would use a get request for retrieving info from a 
# website but this is just how this API endpoint is designed) I want to get 5200 total ads 
# with an offset of 100.

    payload = {"cliente": "jorge"}  

# Take a look at the last parameter in the payload dictionary. This is where the looping variable is found.
# The rest of the code appends the data (sweet, sweet json!) obtained in each post 
# request to the list ads. Once the foor-loop is done and all the ads are downloaded,  
# the data is saved to a json file for later processing.

    response = requests.get(url, json=payload)
    status = response.status_code

    data = json.loads(response.text)
    ads.append(data)
    time.sleep(3) 
# This is just me trying to be nice and not overloading their servers (or get myself 
# banned) by sending to many requests at once. time.sleep(3) introduces a #3-second 
# delay between requests.

with open("raw_ads.json", "w") as f:
    f.write(json.dumps(ads))
