"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for, Blueprint
from api.models import db, User
from api.utils import generate_sitemap, APIException
from flask_jwt_extended import create_access_token
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required

# Create flask app
api = Blueprint('api', __name__)

# Create a route to authenticate your users and return JWTs. The
# create_access_token() function is used to actually generate the JWT.
@api.route("/token", methods=["POST"])
def create_token():
    email = request.json.get("email", None)
    password = request.json.get("password", None)
    if email != "test" or password != "test":
        return jsonify({"msg": "Bad email or password"}), 401

    access_token = create_access_token(identity=email)
    return jsonify(access_token=access_token)


@api.route("/signup", methods=["POST"])
#here i ammmmmmm rocking like a hurricane
def get_email_and_password():
    email = request.json.get('email', None)
    password = request.json.get('password', None)

    #hash the password

    #need to create a list of information to pass to the DB
    our_user = User(
        email = email,
        password = password,
        is_active = False,
    )

    #save the user
    our_user.save_user()

    return jsonify(our_user.serialize())

@api.route("/login", methods=["POST"])
def login_by_email_and_password():
    email = request.json.get('email', None)
    password = request.json.get('password', None)

    #check if exits
    user = check_if_user_exists_and_get_it(email)

    #user = { email, password }
    #user = None

    if user.password == password:

        #create token


    #get the user by email

    return user
    


@api.route("/hello", methods=["GET"])
@jwt_required
def get_hello():
    email = get_jwt_identity()
    dictionary = {
        "message": "Hello World" + email
    }
    return jsonify(dictionary)