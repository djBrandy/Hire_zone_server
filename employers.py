from flask import Blueprint
from flask_restful import Api,Resource,reqparse

employer_bp = Blueprint('employer_bp',__name__,url_prefix='/employer')
api_bp=Api(employer_bp)
employer_parser = reqparse.RequestParser()
employer_parser.add_argument('company_name', type=str, required=True, help='company_name is required')
employer_parser.add_argument('industry', type=str, required=True, help='industry is required')
employer_parser.add_argument('location', type=str, required=True, help='location is required')
employer_parser.add_argument('contact_email', type=str, required=True, help=' contact_email is required')


class Employer(Resource):
    def get(self,id):
        employer = Employer.query.get_or_404(id)
        return {'id': employer.id,'company_name':employer.company_name,"industry":employer.industry,"location":employer.location,"contact_email":employer.contact_email}
    
    def put(self,id):
        data = employer_parser.parse_args()
        employer = Employer.query.get_or_404(id)
        employer.company_name = data['company_name']
        employer.industry = data['industry']
        employer.location = data['location']
        employer.contact_email = data['contact_email']
        db.session.commit()
        return {'id': employer.id,'company_name':employer.company_name,"industry":employer.industry,"location":employer.location,"contact_email":employer.contact_email}
    
    def delete(self,id):
        employer = Employer.query.get_or_404(id)
        db.session.delete(employer)
        db.session.commit()
        return {'message': 'Employer deleted successfully'}


api_bp.add_resource(Employer, '/<int:id>')
   
   
   
   
   
   
   
   
class employersList(Resource): 
    def get(self):
        employers = Employer.query.all()
        return [{'id':emp.id,'company_name':emp.company_name,"industry":emp.industry,"location":emp.location,"contact_email":emp.contact_email} for emp in employers]
    
    def post(self):
        data = employer_parser.parse_args()
        new_employer = Employer(company_name=data['company_name'], industry=data['industry'], location=data['location'], contact_email=data['contact_email'])
        db.session.add(new_employer)
        db.session.commit()
        return {"message": "Employer successfully created"}
    
    def delete(self,id):
        employer=Employer.query.get(id)
        db.session.delete(employer)
        db.session.commit()
        return {'message': ' employer deleted successfully'}
    

api_bp.add_resource(employersList, '/')
       
    
    


