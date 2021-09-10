from MicroservicioPaciente import create_app
from flask_restful import Resource,Api
from flask import Flask, request
import requests
import json
from faker import Faker
import enum
fake = Faker()
import  random
import threading
import urllib.request

app=create_app('default')
app_context = app.app_context()
app_context.push()

api=Api(app)

class Eps(enum.Enum):
   Sanitas = 1
   Sura = 2
   Coomeva = 3
   Famisanar = 4
   Compensar = 5
   Cafam = 6
   Cafesalud = 7

class Paciente(Resource):
    def get(self):
        id = fake.random_int(1, 9999)
        nombre = fake.unique.name()
        fechaNacimiento=str(fake.date())
        direccion=fake.address()
        Epss=["Sanitas", "Sura", "Coomeva", "Famisanar", "Compensar", "Cafam","Cafesalud"]
        Eps = random.choice(list(Epss))
        return {"id" : id, "identificacion":request.json['identificacion'], "nombre": nombre, "fechaNacimiento": fechaNacimiento, "direccion":direccion, "Eps":Eps}

api.add_resource(Paciente, '/paciente')

""""
import platform    # For getting the operating system name
import subprocess  # For executing a shell command

def ping(host):
    """"""
    Returns True if host (str) responds to a ping request.
    Remember that a host may not respond to a ping (ICMP) request even if the host name is valid.
    """"""

    # Option for the number of packets as a function of
    param = '-n' if platform.system().lower()=='windows' else '-c'

    # Building the command. Ex: "ping -c 1 google.com"
    command = ['ping', param, '1', host]

    return subprocess.call(command) == 0

#ping("www.google.com")
timer = threading.Timer(2.0, ping("www.google.com"))
timer.start()
"""
""""
import platform
import subprocess


def myping(host):
    parameter = '-n' if platform.system().lower() == 'windows' else '-c'

    command = ['ping', parameter, '1', host]
    response = subprocess.call(command)

    if response == 0 or response==200:
        return True
    else:
        return False


#api = "http://proyecto-ionic-frontend.herokuapp.com/"
#api2="http://proyecto-ionicidoao_vk2944jfifjd.herokuapp.com/"
#resp = urllib.request.urlopen(api)
#resp2=urllib.request.urlopen(api)
#result = resp.read()
#result = json.loads(result.decode("utf-8"))
#print(result)
print(myping("personas.serviciodeempleo.gov.co/"))
print(myping("proyecto-ionic-frontend.herokuapp.com/canciones/2"))
"""
print(resp)
print(resp.status)
print(resp2)
print(resp2.status)
print(resp.closed)
print(resp2.closed)
#print(myping("www.google.com"))
#print(myping("127.0.0.1:5000/paciente"))
print(myping("personas.serviciodeempleo.gov.co/"))
#print(myping("http://proyecto-ionic-frontend.herokuapp.com/"))
"""
"""
import http.client
conn = http.client.HTTPSConnection("proyecto-ionic.herokuapp.com/canciones/1")
print(conn)
conn.request('GET','/')
conn.send('{nombre:jhon1,contrasena:12345}')
conn.request('POST','/')

r1 = conn.getresponse()
print(r1.status, r1.reason)
conn2 = http.client.HTTPSConnection("proyecto-ionic.herokuapp.com/cancionesfdfee/1")
conn2.request("GET", "/")
r2 = conn2.getresponse()
print(r2.status, r2.reason)"""