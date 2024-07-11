from flask import Blueprint
from flask_restful import Api,Resource,reqparse
from models import db,Jobs,Employer
from flask_cors import CORS

jobs_bp = Blueprint('jobs', __name__,url_prefix='/jobs')
api_bp=Api(jobs_bp)
job_parser = reqparse.RequestParser()
job_parser.add_argument('title', type=str, required=True, help='title is required')
job_parser.add_argument('description', type=str, required=True, help='description is required')
job_parser.add_argument('salary', type=str, required=True, help='salary is required')
job_parser.add_argument('employer_id', type=str, required=True, help='employer_id is required')



CORS(jobs_bp)



class Job(Resource):
    def get(self,id):
        job = Jobs.query.get_or_404(id)
        return {'id': job.id,'title':job.title,"description":job.description,"salary":job.salary,"employer_id":job.employer_id}
    
    def put(self,id):
        data = job_parser.parse_args()
        job = Jobs.query.get_or_404(id)
        job.title = data['title']
        job.description = data['description']
        job.salary = data['salary']
        job.employer_id = data['employer_id']
        db.session.commit()
        return {'id': job.id,'title':job.title,"description":job.description,"salary":job.salary,"employer_id":job.employer_id}
    
    def delete(self,id):
        job = Jobs.query.get_or_404(id)
        db.session.delete(job)
        db.session.commit()
        return {'message': 'Job deleted successfully'}


api_bp.add_resource(Job, '/<int:id>')


class JobsList(Resource):
    def get(self):
        jobs = Jobs.query.all()
        return [{'id': job.id,'title':job.title,"description":job.description,"salary":job.salary,"employer_id":job.employer_id} for job in jobs]
    
    def post(self):
        data = job_parser.parse_args()
        new_job = Jobs(title=data['title'], description=data['description'], salary=data['salary'], employer_id=data['employer_id'])
        db.session.add(new_job)
        db.session.commit()
        return {"message": "Job successfully created"}
    
    def delete(self,id):
        job = Jobs.query.get(id)
        db.session.delete(job)
        db.session.commit()
        return {'message': 'Job deleted successfully'}


api_bp.add_resource(JobsList, '/joblist')

class JobEmployers(Resource):
    def get(self,employer_id):
        job = Jobs.query.get(id)
        if not job:
            return {'message': 'job not found'}, 404
        employer = Employer.query.get(job.employer_id)
        return {'id': employer.id, 'company_name':employer.company_name, 'industry': employer.industry,'contact_email': employer.contact_email}
    


api_bp.add_resource(JobEmployers, '/<int:employer_id>/job')