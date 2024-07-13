from flask import Blueprint
from flask_restful import Api, Resource, reqparse
from models import db, JobSeekersDetails

details_bp = Blueprint('details', __name__, url_prefix='/details')
api = Api(details_bp)

# Define request parser
details_parser = reqparse.RequestParser()
details_parser.add_argument('resume_url', type=str, required=True, help='Resume URL is required')
details_parser.add_argument('skills', type=str, required=True, help='Skills are required')
details_parser.add_argument('education_level', type=str, required=True, help='Education level is required')
details_parser.add_argument('work_experience', type=str, required=True, help='Work experience is required')
details_parser.add_argument('portfolio_url', type=str, required=True, help='Portfolio URL is required')
details_parser.add_argument('jobseeker_id', type=int, required=True, help='Jobseeker ID is required')

class JobSeekersDetailsResource(Resource):
    def post(self):
        data = details_parser.parse_args()
        details = JobSeekersDetails(
            resume_url=data['resume_url'],
            skills=data['skills'],
            education_level=data['education_level'],
            work_experience=data['work_experience'],
            portfolio_url=data['portfolio_url'],
            jobseeker_id=data['jobseeker_id']
        )
        db.session.add(details)
        db.session.commit()
        return {'message': 'Job Seeker details added successfully.'}, 201

    def get(self, jobseeker_id):
        details = JobSeekersDetails.query.filter_by(jobseeker_id=jobseeker_id).first()
        if not details:
            return {'message': 'Job Seeker details not found.'}, 404
        return details.to_dict(), 200

    def put(self, jobseeker_id):
        data = details_parser.parse_args()
        details = JobSeekersDetails.query.filter_by(jobseeker_id=jobseeker_id).first()
        if not details:
            return {'message': 'Job Seeker details not found.'}, 404
        details.jobseeker_id = data['jobseeker_id']
        details.resume_url = data['resume_url']
        details.skills = data['skills']
        details.education_level = data['education_level']
        details.work_experience = data['work_experience']
        details.portfolio_url = data['portfolio_url']
        db.session.commit()
        return details.to_dict(), 200

class AllJobSeekersDetailsResource(Resource):
    def get(self):
        details_list = JobSeekersDetails.query.all()
        return [details.to_dict() for details in details_list], 200

# Add resource routes
api.add_resource(JobSeekersDetailsResource, '/', '/<int:jobseeker_id>')
api.add_resource(AllJobSeekersDetailsResource, '/all')
