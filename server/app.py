from flask import Flask, render_template, jsonify, request
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Resource, Api
from flask_cors import CORS
from flask_marshmallow import Marshmallow
from datetime import datetime
import os

app = Flask(__name__)
CORS(app)
# load settings from the config.py
app.config.from_object(Config)
# for RESTful api
api = Api(app)
#  init db object
db = SQLAlchemy(app)
# marshmallow converting complex datatypes, such as objects, to and from native Python datatypes
ma = Marshmallow(app)

# Setup Users table
class Users(db.Model):
    # Use Column to define a column. 
    id = db.Column('user_id', db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(100), nullable=False)
    status = db.Column(db.String(100), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow)
    deleted_at = db.Column(db.DateTime, default=datetime.utcnow)
# Setup Users Schema
class UsersSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Users
        load_instance = True

# if the database does not exist, use db.create_all()
def initialize_database():
    try:
        Users.query.get(1)
    except:
        db.create_all()
        # put some place holder data
        user1 = Users(name='User1', description='UserDescription1', status='UserStatus1')
        user2 = Users(name='User2', description='UserDescription2', status='UserStatus2')
        # add and then commit to apply changes
        db.session.add(user1)
        db.session.add(user2)
        db.session.commit()
        # delete use: db.session.delete(me)

def query_Users():
    users = Users.query.all()
    users_schema = UsersSchema(many=True)
    # convert the sqlresult into python dictionary that can be jsonify
    output = users_schema.dump(users)
    return output

def modify_Users( id=-1, name='', description='', status='', delete=False):
    if id == -1:
        # if the id is not specified, then we add a new item
        new_user = Users( name=name, description=description, status=status)
        db.session.add(new_user)
    else:
        # if the id already exist, then modify the existing item
        existing_user = Users.query.get(id)
        if delete == True:
            existing_user.deleted_at = datetime.utcnow
            db.session.delete(existing_user)
        else:
            existing_user.name = name
            existing_user.description = description
            existing_user.status = status
            existing_user.updated_at = datetime.utcnow
    # apply changes
    db.session.commit()

class users_database_access(Resource):
    def get(self):
        # the arguments for the function is given by the URL
        # curl http://localhost:5000
        output = query_Users()
        return jsonify(output)
    def post(self):
        # curl http://localhost:5000/ -d "data=wassup" -X POST -v
        # accept argument by parsing the packages
        users_args = request.get_json()
        print(users_args)
        modify_Users(**users_args)
        return jsonify(status='modify success')

api.add_resource(users_database_access, '/users_db')

if __name__ == '__main__':
    initialize_database()
    query_Users()
    app.run(debug=True)