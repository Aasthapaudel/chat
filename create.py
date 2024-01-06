from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from models import db, User  # Make sure to import your models from the models module

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:admin@localhost:5432/rchat'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:admin@localhost:5432/rchat'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    db.init_app(app)
    db.create_all()
    return app

def main():
    with app.app_context():
        db.create_all()

if __name__ == "__main__":
    main()
