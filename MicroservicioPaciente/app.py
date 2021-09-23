from flask_restful import Resource,Api
from flask import Flask, request
from faker import Faker
import enum
import random
from flask_jwt_extended import  JWTManager, jwt_required,create_access_token
import requests

def create_app(config_name):
    app = Flask(__name__)
    app.config['JWT_SECRET_KEY']='frase-secreta'
    app.config['PROPAGATE_EXCEPTIONS']=True
    app.config['JWT_TOKEN_LOCATION'] = ["headers"]
    app.config['JWT_HEADER_NAME'] = ["Authorization"]
    app.config['JWT_HEADER_TYPE'] = ["Bearer"]
    return app

fake = Faker()
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
        headers_dict = {"Authorization": request.json['token_de_acceso']}
        content = requests.get('http://127.0.0.1:5000/autorizador', headers=headers_dict)

        if (content.status_code==200):
            id = fake.random_int(1, 9999)
            nombre = fake.unique.name()
            fechaNacimiento=str(fake.date())
            direccion=fake.address()
            Epss=["Sanitas", "Sura", "Coomeva", "Famisanar", "Compensar", "Cafam","Cafesalud"]
            Eps = random.choice(list(Epss))
            return {"id" : id, "identificacion":request.json['identificacion'], "nombre": nombre, "fechaNacimiento": fechaNacimiento, "direccion":direccion, "Eps":Eps}
        else:
            return {"mensaje": "No se obtuvo autorizacion"},500
    def post(self):
        payload = {'identificacion': request.json['identificacion']}
        content = requests.post('http://127.0.0.1:5000/autorizador', json=payload)
        return {"token_de_acceso": (content.json()['token_de_acceso'])}

api.add_resource(Paciente, '/paciente')
