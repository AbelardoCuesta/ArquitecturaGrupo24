from flask_restful import Resource,Api
from flask import Flask, request
from faker import Faker
import enum
import random
from flask_jwt_extended import  JWTManager, jwt_required,create_access_token


def create_app(config_name):
    app = Flask(__name__)
    app.config['JWT_SECRET_KEY']='frase-secreta'
    app.config['PROPAGATE_EXCEPTIONS']=True
    return app

fake = Faker()
app=create_app('default')
app_context = app.app_context()
app_context.push()

api=Api(app)
jwt=JWTManager(app)
class Certificador(Resource):
    def post(self):
        token_de_acceso=create_access_token(identity=request.json['identificacion'])
        return {"token_de_acceso":token_de_acceso,"identificacion":request.json['identificacion']}

    @jwt_required()
    def get(self):
        return "tienes acceso"

api.add_resource(Certificador, '/autorizador')
