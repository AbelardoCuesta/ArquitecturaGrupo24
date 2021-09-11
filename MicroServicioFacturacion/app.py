from  MicroServicioFacturacion import create_app
from flask_restful import Resource,Api
from flask import Flask, request
import requests
import json
from faker import Faker
from random import randrange
import  random


app=create_app('default')
app_context = app.app_context()
app_context.push()

api=Api(app)

fake = Faker()


class Facturacion(Resource):
    def get(self):

        payload = {'identificacion': request.json['identificacion']}
        content = requests.get('http://127.0.0.1:6000/paciente', json=payload)

        servicios=["cirugia", "examenes", "imagenes", "inyectologia", "medicina interna", "neurologia","traumatologia","hematologia","infectologia"]

        paciente = content.json()
        idFactura = fake.uuid4()
        nombrePaciente = paciente['nombre']
        direccion = paciente['direccion']
        total = fake.pricetag()

        servicioPaciente={}
        listaServicio=[]
        for ser in range(1,randrange(1,10)):
            servicioPaciente = {"idServ" : ser, "servicio":random.choice(list(servicios)), "valor": fake.pricetag()}        
            listaServicio.append(servicioPaciente)
        
        return {"id" : idFactura, "identificacion":request.json['identificacion'], "nombrePaciente": nombrePaciente, "direccion": direccion, "total": total, "servicios":listaServicio}

api.add_resource(Facturacion, '/facturacion')