from flask import Blueprint
from flask_restful import Api, Resource, reqparse
from models import db, Jobs, Employer, JobSeekersDetails
from flask_cors import CORS

form_bp = Blueprint('form', __name__, url_prefix='/form')
api_bp = Api(form_bp)

job_parser = reqparse.RequestParser()
job_parser.add_argument('title', type=str, required=True, help='Title is required')
job_parser.add_argument('description', type=str, required=True, help='Description is required')
job_parser.add_argument('salary', type=str, required=True, help='Salary is required')
job_parser.add_argument('employer_id', type=int, required=True, help='Employer ID is required')

jobseeker_parser = reqparse.RequestParser()
jobseeker_parser.add_argument('name', type=str, required=True, help='Name is required')
jobseeker_parser.add_argument('email', type=str, required=True, help='Email is required')
jobseeker_parser.add_argument('resume_url', type=str, required=True, help='Resume URL is required')
jobseeker_parser.add_argument('skills', type=str, required=True, help='Skills are required')
jobseeker_parser.add_argument('education_level', type=str, required=True, help='Education level is required')
jobseeker_parser.add_argument('work_experience', type=str, required=True, help='Work experience is required')
jobseeker_parser.add_argument('portfolio_url', type=str, required=True, help='Portfolio URL is required')
jobseeker_parser.add_argument('jobseeker_id', type=int, required=True, help='Jobseeker ID is required')

CORS(form_bp)

class Job(Resource):
    def get(self, id):
        job = Jobs.query.get_or_404(id)
        return {'id': job.id, 'title': job.title, 'description': job.description, 'salary': job.salary, 'employer_id': job.employer_id}
    
    def put(self, id):
        data = job_parser.parse_args()
        job = Jobs.query.get_or_404(id)
        job.title = data['title']
        job.description = data['description']
        job.salary = data['salary']
        job.employer_id = data['employer_id']
        db.session.commit()
        return {'id': job.id, 'title': job.title, 'description': job.description, 'salary': job.salary, 'employer_id': job.employer_id}
    
    def delete(self, id):
        job = Jobs.query.get_or_404(id)
        db.session.delete(job)
        db.session.commit()
        return {'message': 'Job deleted successfully'}

api_bp.add_resource(Job, '/<int:id>')

class JobsList(Resource):
    def get(self):
        jobs = Jobs.query.all()
        return [{'id': job.id, 'title': job.title, 'description': job.description, 'salary': job.salary, 'employer_id': job.employer_id} for job in jobs]
    
    def post(self):
        data = job_parser.parse_args()
        new_job = Jobs(title=data['title'], description=data['description'], salary=data['salary'], employer_id=data['employer_id'])
        db.session.add(new_job)
        db.session.commit()
        return {"message": "Job successfully created"}, 201

api_bp.add_resource(JobsList, '/joblist')

class JobEmployers(Resource):
    def get(self, employer_id):
        employer = Employer.query.get_or_404(employer_id)
        return {'id': employer.id, 'company_name': employer.company_name, 'industry': employer.industry, 'contact_email': employer.contact_email}

api_bp.add_resource(JobEmployers, '/<int:employer_id>/job')

class JobSeekers(Resource):
    def post(self):
        data = jobseeker_parser.parse_args()
        new_jobseeker = JobSeekersDetails(
            name=data['name'],
            email=data['email'],
            resume_url=data['resume_url'],
            skills=data['skills'],
            education_level=data['education_level'],
            work_experience=data['work_experience'],
            portfolio_url=data['portfolio_url'],
            jobseeker_id=data['jobseeker_id']
        )
        db.session.add(new_jobseeker)
        db.session.commit()
        return {"message": "Job seeker details successfully created"}, 201

api_bp.add_resource(JobSeekers, '/jobseekers')

# Make sure to register the blueprint in your main application file
# For example in app.py or main.py
from flask import Flask
# from yourmodule import form_bp, db

app = Flask(__name__)
# Configure your database here
# app.config['SQLALCHEMY_DATABASE_URI'] = 'your_database_uri'
# db.init_app(app)
app.register_blueprint(form_bp)

if __name__ == '__main__':
    app.run(debug=True)
