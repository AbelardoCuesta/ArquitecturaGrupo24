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