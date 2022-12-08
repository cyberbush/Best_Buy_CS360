from flask import Flask, render_template, jsonify, request, Blueprint
from flask_sqlalchemy import SQLAlchemy
from config import Config
from flask_restful import Resource, Api
from flask_cors import CORS
from flask_marshmallow import Marshmallow
from datetime import datetime
# from passlib.apps import custom_app_context as pwd_context
import os

#-------------------------------------------
#------------------ Setup ------------------
#-------------------------------------------
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
#-------------------------------------------
#---------------- End Setup ----------------
#-------------------------------------------

#-------------------------------------------
#------------------ Tables -----------------
#-------------------------------------------
# Class for users
class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    firstName = db.Column(db.String(50), nullable=False)
    lastName = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(50), nullable=False)
    options = db.Column(db.JSON, nullable=False)
# Setup User Schema
class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User
        load_instance = True

# Class for Vendors
class Vendor(db.Model):
    __tablename__ = 'vendors'
    id = db.Column(db.Integer, primary_key=True)
    firstName = db.Column(db.String(50), nullable=False)
    lastName = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(50), nullable=False)
# Setup Vendor Schema
class VendorSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Vendor
        load_instance = True

# Setup products table
class Products(db.Model):
    # Use Column to define a column. 
    id = db.Column('product_id', db.Integer, primary_key=True)
    vendorId = db.Column(db.Integer, nullable=False)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)
    category = db.Column(db.String(100), nullable=False)
    brand = db.Column(db.String(100), nullable=False)
    size = db.Column(db.Float, nullable=False)
# Setup products Schema
class ProductsSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Products
        load_instance = True

# Setup Offers table
class Offers(db.Model):
    # Use Column to define a column. 
    id = db.Column(db.Integer, primary_key=True)
    vendor = db.Column(db.JSON, nullable=False)
    user = db.Column(db.JSON, nullable=False)
    product = db.Column(db.JSON, nullable=False)
    penalty = db.Column(db.Float, nullable=False)
    vendorAccept = db.Column(db.Boolean, nullable=False, default=False)
    userAccept = db.Column(db.Boolean, nullable=False, default=True)
# Setup Offers Schema
class OffersSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Offers
        load_instance = True
#-------------------------------------------
#---------------- End Tables ---------------
#-------------------------------------------

#-------------------------------------------
#------------ Utility Functions ------------
#-------------------------------------------
# if the database does not exist, use db.create_all()
def initialize_database():
    try:
        User.query.get(1) and Vendor.query.get(1) and Products.query.get(1) and Offers.query.get(1) 
    except:
        db.create_all()
        # Add initial user
        option1 = {'category': False, 'price': False, 'description': False, 'brand': False, 'size': False}
        user1 = User(firstName='Joe', lastName='Vandal', email='joe@vandal.com', password='123', options=option1)
        db.session.add(user1)        
        # Add initial vendor
        vendor1 = Vendor(firstName='Vendor1', lastName='V', email='vendor1@gmail.com', password='123')
        db.session.add(vendor1)  
        # Add initial products
        product1 = Products(vendorId=1, name='product1', price=0.0, description='productDescription1', brand='productBrand1', category='Electronics', size=0.0)
        product2 = Products(vendorId=2, name='product2', price=0.0, description='productDescription2', brand='productBrand2', category='Electronics', size=0.0)
        db.session.add(product1)
        db.session.add(product2)
        db.session.commit()
        # Add initial offer
        offer1 = Offers(vendor=VendorSchema().dump(vendor1), user=UserSchema().dump(user1), product=ProductsSchema().dump(product1), penalty=50)
        db.session.add(offer1)  
        # add and then commit to apply changes
        db.session.commit()

def query_users():
    users = User.query.all()
    users_schema = UserSchema(many=True)
    # convert the sql result into python dictionary that can be jsonify
    output = users_schema.dump(users)
    return output

def find_user(id):
    user = User.query.get(id)
    user_out = UserSchema().dump(user)
    return user_out    

def query_vendors():
    vendors = Vendor.query.all()
    vendors_schema = VendorSchema(many=True)
    # convert the sql result into python dictionary that can be jsonify
    output = vendors_schema.dump(vendors)
    return output

def find_vendor(id):
    vendor = Vendor.query.get(id)
    vendor_out = VendorSchema().dump(vendor)
    return vendor_out    

def query_products():
    products = Products.query.all()
    products_schema = ProductsSchema(many=True)
    # convert the sql result into python dictionary that can be jsonify
    output = products_schema.dump(products)
    return output

def find_product(id):
    product = Products.query.get(id)
    product_out = ProductsSchema().dump(product)
    # print('Product: ', product_out)
    return product_out

def query_offers():
    offers = Offers.query.all()
    offers_schema = OffersSchema(many=True)
    # convert the sql result into python dictionary that can be jsonify
    output = offers_schema.dump(offers)
    return output

def modify_users( id=-1, email='', firstName='', lastName='', password='', options=None, delete=False):
    if id == -1:
        # if the id is not specified, then we add a new user
        if email is None or password is None:
            os.abort(400) # missing arguments
        if User.query.filter_by(email = email).first() is not None:
            os.abort(400) # existing user
        option = {'category': False, 'price': False, 'description': False, 'brand': False, 'size': False}
        new_user = User(email = email, firstName=firstName, lastName=lastName, password=password, options=option)
        db.session.add(new_user)
    else:
        # if the id already exist, then modify the existing item
        existing_user = User.query.get(id)
        if delete == True:
            db.session.delete(existing_user)
        elif options: # add preferences
            existing_user.options = options
        else:
            existing_user.firstName = firstName
            existing_user.lastName = lastName
            existing_user.email = email
            existing_user.password = password
    # apply changes
    db.session.commit()

def modify_vendors( id=-1, email='', firstName='', lastName='', password='', delete=False):
    if id == -1:
        # if the id is not specified, then we add a new vendor
        if email is None or password is None:
            os.abort(400) # missing arguments
        if Vendor.query.filter_by(email = email).first() is not None:
            os.abort(400) # existing vendor
        new_vendor = Vendor(email = email, firstName=firstName, lastName=lastName, password=password)
        db.session.add(new_vendor)
    else:
        # if the id already exist, then modify the existing item
        existing_vendor = Vendor.query.get(id)
        if delete == True:
            db.session.delete(existing_vendor)
        else:
            existing_vendor.firstName = firstName
            existing_vendor.lastName = lastName
            existing_vendor.email = email
            existing_vendor.password = password
    # apply changes
    db.session.commit()

def modify_products( id=-1, vendorId=0, name='', price=0.0, size=0.0, description='', category='', brand='', delete=False):
    if id == -1:
        # if the id is not specified, then we add a new item
        new_product = Products( vendorId=vendorId, name=name, price=price, size=size, description=description, category=category, brand=brand)
        db.session.add(new_product)
    else:
        # if the id already exist, then modify the existing item
        existing_product = Products.query.get(id)
        if delete == True:
            db.session.delete(existing_product)
        else:
            existing_product.name = name
            existing_product.description = description
            existing_product.price = price
            existing_product.size = size
            existing_product.brand = brand
            existing_product.category = category
    # apply changes
    db.session.commit()

def modify_offers(id=0, userId=0, productId=0, penalty=0.0, vendorAccept=False, userAccept=False, delete=False):
    if delete == True:
        existing_offer = Offers.query.get(id)
        db.session.delete(existing_offer)
    else:
        user = find_user(userId)
        product = find_product(productId)
        vendor = find_vendor(product['vendorId'])
        new_offer = Offers( vendor=vendor, user=user, product=product, penalty=penalty, vendorAccept=vendorAccept, userAccept=userAccept)
        db.session.add(new_offer)
    # apply changes
    db.session.commit()

def calculate_matches(id=-1):
    if id == -1: # Error
        return jsonify(status='Error no user found')
    else:
        exactProd = {'id': 0, 'score': 0}
        user = find_user(id)
        options = user['options']
        products = query_products()
        for product in products: # go through all products
            exactScore = 0
            for option in options: # go through options and check if they match product
                opt_val = options[option]
                prod_val = product[option]
                if opt_val: # if option is set 
                    if option == 'price' and prod_val <= opt_val: # price of product less or equal to price of option
                        exactScore += 1                        
                    elif option == 'description' and opt_val in prod_val: # option description substring of product description
                        exactScore += 1
                    elif product[option] == options[option]: # if product and option match
                        exactScore += 1
            if exactScore >= exactProd['score']: # check and update exact product
                exactProd['id'] = product['id']
                exactProd['score'] = exactScore
        exactMatch = find_product(exactProd['id'])
        return exactMatch

#-------------------------------------------
#---------- End Utility Functions ----------
#-------------------------------------------

#-------------------------------------------
#------------------ APIs -------------------
#-------------------------------------------

@app.route('/api/users', methods = ['GET', 'POST'])
def users():
    if request.method == 'GET':
        output = query_users()
        return jsonify(output)
    elif request.method == 'POST':
        user_args = request.get_json()
        # print(user_args)
        modify_users(**user_args)
        return jsonify(status='modify success')

@app.route('/api/users/login', methods = ['POST'])
def loginUser():
    email = request.json.get('email')
    password = request.json.get('password')
    user = User.query.filter_by(email = email).first()
    if not user or user.password != password:
        return jsonify({'Error':'Enter wrong password or username'})
    user_schema = UserSchema()
    output = user_schema.dump(user)
    return jsonify(output)

@app.route('/api/vendors', methods = ['GET', 'POST'])
def vendors():
    if request.method == 'GET':
        output = query_vendors()
        return jsonify(output)
    elif request.method == 'POST':
        vendor_args = request.get_json()
        # print(vendor_args)
        modify_vendors(**vendor_args)
        return jsonify(status='modify success')

@app.route('/api/vendors/login', methods = ['POST'])
def loginVendor():
    email = request.json.get('email')
    password = request.json.get('password')
    vendor = Vendor.query.filter_by(email = email).first()
    if not vendor or vendor.password != password:
        return jsonify({'Error':'Enter wrong password or username'})
    vendor_schema = VendorSchema()
    output = vendor_schema.dump(vendor)
    return jsonify(output)

@app.route('/api/products', methods = ['GET', 'POST'])
def products():
    if request.method == 'GET': 
        args = request.args
        # print(args)
        if args: # return single product
            product_Id = args.get('productId')
            # print(product_Id)
            product = find_product(product_Id)
            return product
        else: # return all products
            output = query_products()
            return jsonify(output)
    elif request.method == 'POST':
        products_args = request.get_json()
        # print(products_args)
        modify_products(**products_args)
        return jsonify(status='modify success')

@app.route('/api/offers', methods = ['GET', 'POST'])
def offers():
    if request.method == 'GET':
        output = query_offers()
        return jsonify(output)
    elif request.method == 'POST':
        offers_args = request.get_json()
        # print(offers_args)
        modify_offers(**offers_args)
        return jsonify(status='modify success')

@app.route('/api/match', methods = ['POST'])
def match():
    match_args = request.get_json()
    # print(offers_args)
    matched_products = calculate_matches(**match_args)
    return jsonify(matched_products)

#-------------------------------------------
#---------------- End APIs -----------------
#-------------------------------------------

#-------------------------------------------
#------------------ Main -------------------
#-------------------------------------------
if __name__ == '__main__':
    with app.app_context():
        initialize_database()
        # query_products()
        app.run(debug=True)
#-------------------------------------------
#---------------- End Main -----------------
#-------------------------------------------