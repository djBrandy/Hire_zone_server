from flask import Blueprint
from flask_restful import Api,Resource,reqparse

employer_bp = Blueprint('employer_bp',__name__,url_prefix='/employer')
api_bp=Api(employer_bp)



class Employer(Resource):
    def get(self):
        return {'message': 'Employer endpoint'}
    

