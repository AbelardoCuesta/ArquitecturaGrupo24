import random

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
        numero=random.randint(1,10)
        print(numero)
        if (numero<=7):
            payload = {'identificacion': request.json['identificacion']}
            content = requests.get('http://127.0.0.1:7000/facturacion', json=payload)
            facturacion = content.json()
            facturaId = facturacion['id']
            total = facturacion['total']
            estadoPago = fake.pybool()
            fechaSalida = str(datetime.now())[:19]
            cambioDinero = fake.pricetag()
            fecha = str(datetime.now())[:19]
            logData = fecha + " : microservicio salida opera normalmente, respuesta exitosa al monitor " + facturaId
            return {"estadoPago": estadoPago, "fechaSalida": fechaSalida, "cambioDinero": cambioDinero, "facturaId": facturaId},content.status_code
        else:
            payload = {'identificacion': request.json['identificacion']}
            content = requests.get('http://127.0.0.1:7000/facturacion', json=payload)
            facturacion = content.json()
            facturaId = facturacion['id']
            total = facturacion['total']
            estadoPago = fake.pybool()
            fechaSalida = str(datetime.now())[:19]
            cambioDinero = fake.pricetag()
            fecha = str(datetime.now())[:19]
            logData = fecha + " : microservicio salida opera normalmente, respuesta exitosa al monitor " + facturaId
            return {"estadoPago": estadoPago, "fechaSalida": fechaSalida, "cambioDinero": cambioDinero,
                    "facturaId": facturaId}, 500


class VistaEcho(Resource):

    def get(self):
        id = request.json["cliente"]
        fecha = str(datetime.now())[:19]
        logData = fecha + " : microservicio salida opera normalmente, respuesta exitosa al monitor " + id
        return "logData", 200

api.add_resource(VistaSalida, '/salida')
api.add_resource(VistaEcho, '/echo')
