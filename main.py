from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app= Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Hire-zone.db'
# create database called jobs
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
migrate = Migrate(app=app, db=db)





if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5050, debug=True)