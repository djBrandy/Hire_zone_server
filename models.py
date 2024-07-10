from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData


metadata = MetaData(naming_convention={
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
})

db = SQLAlchemy( metadata=metadata)


class Employer(db.Model):
    __tablename__ = 'employers_table'

    id = db.Column(db.Integer, primary_key=True)
    company_name = db.Column(db.String, nullable=False)
    industry = db.Column(db.String, nullable=False)
    location = db.Column(db.String, nullable=False)
    contact_email = db.Column(db.String, nullable=False)
    jobs = db.relationship('Job', backref='employer', lazy=True)
    
    job_seekers = db.relationship('JobSeekers', secondary='employer_job_seekers', backref=db.backref('employers', lazy=True))

    def __repr__(self):
        return f"Employer with the ID of {self.id}, company name of {self.company_name} and the industry of {self.industry} successfully created."


class JobSeekers(db.Model):
    __tablename__ = 'job_seekers_table'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String, nullable=False)
    last_name = db.Column(db.String, nullable=False)
    middle_name = db.Column(db.String)
    email = db.Column(db.String, nullable=False)
    phone_number = db.Column(db.String, nullable=False)
    def __repr__(self):
        return f"Job Seeker with the ID of {self.id}, and name of {self.first_name} {self.last_name} successfully created."


class JobSeekersDetails(db.Model):
    __tablename__ = 'job_seekers_details'

    id = db.Column(db.Integer, primary_key=True)
    resume_url = db.Column(db.String, nullable=False)
    skills = db.Column(db.String, nullable=False)
    education_level = db.Column(db.String, nullable=False)
    work_experience = db.Column(db.String, nullable=False)
    portfolio_url = db.Column(db.String, nullable=False)
    jobseeker_id = db.Column(db.Integer, db.ForeignKey('job_seekers_table.id'), unique=True, nullable=False)

    # Establish back reference to JobSeekers
    job_seeker = db.relationship('JobSeekers', back_populates='details')
    employers = db.relationship('Employer', secondary='employer_job_seekers', backref=db.backref('job_seekers', lazy=True))

    def __repr__(self):
        return "Job Seeker's details added successfully."


    def __repr__(self):
        return "Job Seeker's details added successfully."


class Jobs(db.Model):
    __tablename__ = 'jobs_table'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=False)
    salary = db.Column(db.Integer, nullable=False)
    employer_id = db.Column(db.Integer, db.ForeignKey('employers_table.id'), nullable=False)

    def __repr__(self):
        return f"Job with the ID of {self.id}, title of {self.title} created successfully."


class EmployerJobSeekersConnector(db.Model):
    __tablename__ = 'employer_job_seekers'

    id = db.Column(db.Integer, primary_key=True)
    employer_id = db.Column(db.Integer, db.ForeignKey('employers_table.id'), nullable=False)
    job_seeker_id = db.Column(db.Integer, db.ForeignKey('job_seekers_table.id'), nullable=False)

    def __repr__(self):
        return f"EmployerJobSeekersConnector between employer ID {self.employer_id} and job seeker ID {self.job_seeker_id} created successfully."


