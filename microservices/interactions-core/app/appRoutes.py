from flask import Flask
from flask_restful import Api
from . import appHandlers
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
api = Api(app=app, prefix='/api/v1')


api.add_resource(appHandlers.Main, "")
api.add_resource(appHandlers.Registry,"/registry")