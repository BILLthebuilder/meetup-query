from flask import Flask, Blueprint, jsonify, request, make_response
from ..models import user_models
from werkzeug.security import generate_password_hash, check_password_hash
from ..utils.validators import UserValidation

user_v1 = Blueprint("auth", __name__, url_prefix='/api/v1')
users = user_models.UserModel()
validator = UserValidation()


@user_v1.route('/signup', methods=['POST'])
def signup():
    """ An endpoint for registration of new users """

    try:
        data = request.get_json()
    except:
        return make_response(jsonify({
            "status": 400,
            "message": "Incorrect input"
        })), 400
    
    firstname = data.get('firstname')
    lastname = data.get('lastname')
    othername = data.get('othername')
    email = data.get('email')
    phoneNumber = data.get('phoneNumber')
    username = data.get('username')
    isAdmin = data.get('isAdmin')
    password = data.get('password')

    if not firstname:
        return make_response(jsonify({
            "status": 400,
            "message": "Your first name is required"
        })), 400
    if not lastname:
        return make_response(jsonify({
            "status": 400,
            "message": "Your last name is required"
        })), 400
    if not email:
        return make_response(jsonify({
            "status": 400,
            "message": "Please enter your email"
        })), 400
    if not phoneNumber:
        return make_response(jsonify({
            "status": 400,
            "message": "The phonenumber is required"
        })), 400
    if not username:
        return make_response(jsonify({
            "status": 400,
            "message": "Your username is required"
        })), 400
    if not password:
        return make_response(jsonify({
            "status": 400,
            "message": "Your password is required"
        })), 400

    if validator.validate_password(password):
        return make_response(jsonify({
            "status": 400,
            "message": "Your password is invalid"
        })), 400

    if not validator.validate_email(email):
        return make_response(jsonify({
            "status": 400,
            "message": "Invalid email"
        })), 400

    if validator.username_exists(username):
        return make_response(jsonify({
            "status": 400,
            "message": "Username already exists"
        })), 400

    if validator.email_exists(email):
        return make_response(jsonify({
            "status": 400,
            "message": "That email already exists"
        })), 400

    password = generate_password_hash(
        password, method='pbkdf2:sha256', salt_length=8)

    return make_response(jsonify({
        "status": 201,
        "data": [{
            "firstname": firstname,
            "lastname": lastname,
            "othername": othername,
            "email": email,
            "phoneNumber": phoneNumber,
            "username": username,
            "isAdmin": isAdmin,
        }]
    })), 201