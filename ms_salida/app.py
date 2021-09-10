from ms_salida import create_app
from flask_restful import Resource, Api
from flask import Flask, request
from faker import Faker
from datetime import datetime
import requests
import json

fake = Faker()

app = create_app('default')
app_context = app.app_context()
app_context.push()

api = Api(app)


class VistaSalida(Resource):
    def get(self):
        estadoPago = fake.pybool()
        print(estadoPago)
        fechaSalida = str(datetime.now())[:19]
        print(fechaSalida)
        cambioDinero = fake.random_int(1, 999)
        print(cambioDinero)
        facturaId = fake.uuid4()
        print(facturaId)
        return {"estadoPago": estadoPago, "fechaSalida": fechaSalida, "cambioDinero": cambioDinero, "facturaId": facturaId}


api.add_resource(VistaSalida, '/salida')
