##### Add form for applyin for jobs
### Needs another frontend component


from flask import Blueprint
from flask_restful import Api,Resource,reqparse
from models import db,JobSeekers
from flask_cors import CORS

jobseeker_bp = Blueprint('jobsekeer_bp',__name__,url_prefix='/jobseekers')
api_bp=Api(jobseeker_bp)
jobseeker_parser = reqparse.RequestParser()
jobseeker_parser.add_argument('first_name', type=str, required=True, help='name is required')
jobseeker_parser.add_argument('middle_name', type=str, required=True, help='middle_name is required')
jobseeker_parser.add_argument('last_name', type=str, required=True, help='last_name is required')
jobseeker_parser.add_argument('email', type=str, required=True, help='email is required')
jobseeker_parser.add_argument('phone_number', type=str, required=True, help='phone_number is required')

CORS(jobseeker_bp)


class Jobseeker(Resource):
    def get(self,id):
        jobseeker = JobSeekers.query.get_or_404(id)
        return {'id': jobseeker.id,'first_name':jobseeker.first_name,"middle_name":jobseeker.middle_name,"last_name":jobseeker.last_name,"email":jobseeker.email,"phone_number":jobseeker.phone_number}
    
    def put(self,id):
        data = jobseeker_parser.parse_args()
        jobseeker = JobSeekers.query.get_or_404(id)
        jobseeker.first_name = data['first_name']
        jobseeker.middle_name = data['middle_name']
        jobseeker.last_name = data['last_name']
        jobseeker.email = data['email']
        jobseeker.phone_number = data['phone_number']
        db.session.commit()
        return {'id': jobseeker.id,'first_name':jobseeker.first_name,"middle_name":jobseeker.middle_name,"last_name":jobseeker.last_name,"email":jobseeker.email,"phone_number":jobseeker.phone_number}
    
    def delete(self,id):
        jobseeker = JobSeekers.query.get_or_404(id)
        db.session.delete(jobseeker)
        db.session.commit()
        return {'message': 'Jobseeker deleted successfully'}


api_bp.add_resource(Jobseeker, '/<int:id>')


class JobseekersList(Resource):
    def get(self):
        jobseekers = JobSeekers.query.all()
        return [{'id':jobseeker.id,'first_name':jobseeker.first_name,"middle_name":jobseeker.middle_name,"last_name":jobseeker.last_name,"email":jobseeker.email,"phone_number":jobseeker.phone_number} for jobseeker in jobseekers]
    
    def post(self):
        data = jobseeker_parser.parse_args()
        new_jobseeker = Jobseeker(first_name=data['first_name'], middle_name=data['middle_name'], last_name=data['last_name'], email=data['email'], phone_number=data['phone_number'])
        db.session.add(new_jobseeker)
        db.session.commit()
        return {"message": "Jobseeker successfully created"}
    
    def delete(self,id):
        jobseeker = JobSeekers.query.get(id)
        db.session.delete(jobseeker)
        db.session.commit()
        return {'message': 'Jobseeker deleted successfully'}
    

api_bp.add_resource(JobseekersList, '/')
                