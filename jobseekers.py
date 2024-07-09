from flask import Blueprint
from flask_restful import Api,Resource,reqparse

jobseeker_bp = Blueprint('employer_bp',__name__,url_prefix='/jobseekers')
api_bp=Api(jobseeker_bp)
jobseeker_parser = reqparse.RequestParser()
jobseeker_parser.add_argument('name', type=str, required=True, help='name is required')
jobseeker_parser.add_argument('email', type=str, required=True, help='email is required')