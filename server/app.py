from flask import Flask, render_template, jsonify, request, Blueprint
from flask_sqlalchemy import SQLAlchemy
from config import Config
from flask_restful import Resource, Api
from flask_cors import CORS
from flask_marshmallow import Marshmallow
from datetime import datetime
from passlib.apps import custom_app_context as pwd_context
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

# Class for users
class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    firstName = db.Column(db.String(50), nullable=False)
    lastName = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(50), nullable=False)
    # password_hash = db.Column(db.String(128))
    # def hash_password(self, password):
    #     self.password_hash = pwd_context.encrypt(password)

    # def verify_password(self, password):
    #     return pwd_context.verify(password, self.password_hash)

# Setup User Schema
class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User
        load_instance = True

# Setup products table
class Products(db.Model):
    # Use Column to define a column. 
    id = db.Column('product_id', db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)
    category = db.Column(db.String(100), nullable=False)
    status = db.Column(db.String(100), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow)
    deleted_at = db.Column(db.DateTime, default=datetime.utcnow)
# Setup products Schema
class ProductsSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Products
        load_instance = True

# if the database does not exist, use db.create_all()
def initialize_database():
    try:
        Products.query.get(1)
        User.query.get(1)
    except:
        db.create_all()
        # put some place holder data
        product1 = Products(name='product1', price=0.0, description='productDescription1', category='category1', status='productStatus1')
        product2 = Products(name='product2', price=0.0, description='productDescription2', category='category1', status='productStatus2')
        db.session.add(product1)
        db.session.add(product2)
        # put some place holder data
        user1 = User(firstName='Joe', lastName='Vandal', email='joe@vandal.com', password='123456')
        db.session.add(user1)
        # add and then commit to apply changes
        db.session.commit()

def query_products():
    products = Products.query.all()
    products_schema = ProductsSchema(many=True)
    # convert the sqlresult into python dictionary that can be jsonify
    output = products_schema.dump(products)
    return output

def query_users():
    users = User.query.all()
    users_schema = UserSchema(many=True)
    # convert the sqlresult into python dictionary that can be jsonify
    output = users_schema.dump(users)
    return output

def modify_products( id=-1, name='', price=0.0, description='', category='', status='', delete=False):
    if id == -1:
        # if the id is not specified, then we add a new item
        new_product = Products( name=name, price=price, description=description, category=category, status=status)
        db.session.add(new_product)
    else:
        # if the id already exist, then modify the existing item
        existing_product = Products.query.get(id)
        if delete == True:
            existing_product.deleted_at = datetime.utcnow
            db.session.delete(existing_product)
        else:
            existing_product.name = name
            existing_product.description = description
            existing_product.price = price
            existing_product.status = status
            existing_product.category = category
            existing_product.updated_at = datetime.utcnow
    # apply changes
    db.session.commit()

class products_database_access(Resource):
    def get(self):
        output = query_products()
        return jsonify(output)
    def post(self):
        products_args = request.get_json()
        print(products_args)
        modify_products(**products_args)
        return jsonify(status='modify success')

api.add_resource(products_database_access, '/products_db')

@app.route('/api/users', methods = ['GET', 'POST'])
def get_users():
    if request.method == 'GET':
        output = query_users()
        return jsonify(output)
    elif request.method == 'POST':
        user = request.get_json()
        existing_user = User.query.get(user['id'])
        if user['delete'] == True:
            db.session.delete(existing_user)
            db.session.commit()
        return jsonify(status='deleted success')

@app.route('/api/signup', methods = ['POST'])
def new_user():
    email = request.json.get('email')
    firstName = request.json.get('firstName')
    lastName = request.json.get('lastName')
    password = request.json.get('password')
    if email is None or password is None:
        os.abort(400) # missing arguments
    if User.query.filter_by(email = email).first() is not None:
        os.abort(400) # existing user
    new_user = User(email = email, firstName=firstName, lastName=lastName, password=password)
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'user':new_user.firstName, 'status':'add user success'})

@app.route('/api/login', methods = ['POST'])
def login():
    email = request.json.get('email')
    password = request.json.get('password')
    user = User.query.filter_by(email = email).first()
    if not user or user.password != password:
        return jsonify({'Error':'Enter wrong password or username'})
    user_schema = UserSchema()
    output = user_schema.dump(user)
    return jsonify(output)

if __name__ == '__main__':
    initialize_database()
    query_products()
    app.run(debug=True)