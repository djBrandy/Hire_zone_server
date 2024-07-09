from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from employers import  employer_bp
from jobseekers import jobseeker_bp

app= Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Hire-zone.db'
# create database called jobs
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.register_blueprint(employer_bp)
app.register_blueprint(jobseeker_bp)
db = SQLAlchemy(app)
migrate = Migrate(app=app, db=db)





if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5050, debug=True)