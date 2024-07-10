from flask import Blueprint
from flask_restful import Api,Resource,reqparse
from models import db,Jobs
jobs_bp = Blueprint('jobs', __name__,url_prefix='/jobs')
api_bp=Api(jobs_bp)
job_parser = reqparse.RequestParser()
job_parser.add_argument('title', type=str, required=True, help='title is required')
job_parser.add_argument('description', type=str, required=True, help='description is required')
job_parser.add_argument('location', type=str, required=True, help='location is required')
job_parser.add_argument('requirements', type=str, required=True, help='requirements is required')


class Job(Resource):
    def get(self,id):
        job = Jobs.query.get_or_404(id)
        return {'id': job.id,'title':job.title,"description":job.description,"location":job.location,"requirements":job.requirements}
    
    def put(self,id):
        data = job_parser.parse_args()
        job = Jobs.query.get_or_404(id)
        job.title = data['title']
        job.description = data['description']
        job.location = data['location']
        job.requirements = data['requirements']
        db.session.commit()
        return {'id': job.id,'title':job.title,"description":job.description,"location":job.location,"requirements":job.requirements}
    
    def delete(self,id):
        job = Jobs.query.get_or_404(id)
        db.session.delete(job)
        db.session.commit()
        return {'message': 'Job deleted successfully'}


api_bp.add_resource(Job, '/<int:id>')


class JobsList(Resource):
    def get(self):
        jobs = Jobs.query.all()
        return [{'id': job.id,'title':job.title,"description":job.description,"location":job.location,"requirements":job.requirements} for job in jobs]
    
    def post(self):
        data = job_parser.parse_args()
        new_job = Jobs(title=data['title'], description=data['description'], location=data['location'], requirements=data['requirements'])
        db.session.add(new_job)
        db.session.commit()
        return {"message": "Job successfully created"}
    
    def delete(self,id):
        job = Jobs.query.get(id)
        db.session.delete(job)
        db.session.commit()
        return {'message': 'Job deleted successfully'}


api_bp.add_resource(JobsList, '/joblist')