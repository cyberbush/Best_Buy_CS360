from unicodedata import category
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
    except:
        db.create_all()
        # put some place holder data
        product1 = Products(name='product1', price=0.0, description='productDescription1', category='category1', status='productStatus1')
        product2 = Products(name='product2', price=0.0, description='productDescription2', category='category1', status='productStatus2')
        # add and then commit to apply changes
        db.session.add(product1)
        db.session.add(product2)
        db.session.commit()
        # delete use: db.session.delete(me)

def query_products():
    products = Products.query.all()
    products_schema = ProductsSchema(many=True)
    # convert the sqlresult into python dictionary that can be jsonify
    output = products_schema.dump(products)
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
        # the arguments for the function is given by the URL
        # curl http://localhost:5000
        output = query_products()
        return jsonify(output)
    def post(self):
        # curl http://localhost:5000/ -d "data=wassup" -X POST -v
        # accept argument by parsing the packages
        products_args = request.get_json()
        print(products_args)
        modify_products(**products_args)
        return jsonify(status='modify success')

api.add_resource(products_database_access, '/products_db')

if __name__ == '__main__':
    initialize_database()
    query_products()
    app.run(debug=True)