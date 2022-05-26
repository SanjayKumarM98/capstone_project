import random
import ssl
import string

import jwt

from authentication.models import *
from common.common_modules import *


def login_views(request):
    payload = request.json

    if not payload or not payload['email'] or not payload['password']:
        return make_response('Could Not Verify', 401, {'WWW-Authenticate': 'Basic Realm="Login Required"'})

    user = AuthenticateModels.query.filter_by(email=payload['email']).first()

    if not user:
        return make_response('Could Not Verify', 401, {'WWW-Authenticate': 'Basic Realm="User Does Not Exists'})

    if check_password_hash(user.password, payload['password']):
        token = jwt.encode(
            {'id':user.id, 'email': user.email, 'exp': (datetime.utcnow() + timedelta(days=0, hours=24)).strftime('%Y%m%d%H%M%S')},
            app.config['SECRET_KEY'])
        return make_response(jsonify({'token': token}), 201)

    # returns 403 if password is wrong
    return make_response('Could not verify', 403, {'WWW-Authenticate': 'Basic realm ="Wrong Password !!"'})


def signup_views(request):
    data = request.json

    first_name = data['first_name']
    last_name = data['last_name']
    password = data['password']
    email = data['email']
    gender = data['gender']
    dob = data['dob']

    user = AuthenticateModels.query.filter_by(email=email).first()

    if not user:
        now = datetime.now()
        created_date = now.strftime("%d-%m-%Y %H:%M:%S")

        user = AuthenticateModels(first_name=first_name, last_name=last_name, email=email,
                                  gender=gender, dob=dob, password=generate_password_hash(password),
                                  created_at=created_date)

        if add_data(user):
            return jsonify({'message': 'Successfully Registered!!!'}), 201
        return jsonify({'message': 'not able to add new user details to db'})

    else:
        return jsonify({'message': 'User Already Exists!!!'}), 201


def reset_views(request):
    try:
        payload = request.json
        user = AuthenticateModels.query.filter_by(email=payload['email'], forgot_code=payload['forgot_code']).first()
        if user is not None:
            user.password = generate_password_hash(payload['password'])
            update_data(user)
            return jsonify({'Message': 'Password Reset Is Done'})
        return jsonify({'Message': 'Error While Resetting Password'})
    except Exception as e:
        print("Reset Password", e)
        return jsonify({'Message': 'Error In Reset Password Code'})


def reset_password_mail_views(request):
    try:
        payload = request.json
        user = AuthenticateModels.query.filter_by(email=payload['email']).first()
        if user is not None:
            length = 7  # Length of forgot_code
            ran_code = ''.join(random.choices(string.digits, k=length))
            user.forgot_code = ran_code
            update_data(user)

            msg = Message('Reset Password', sender='sanjay@divum.in', recipients=[payload['email']])
            msg.body = "Hi, Please use the seven digits code sent here as forgot_code to reset your password. " + ran_code
            mail.send(msg)

            return jsonify({'message': 'mail sent'})
        return jsonify({'message': 'Not a registered User'})
    except Exception as e:
        # Print any error messages to stdout
        print(e)
    return jsonify({'message': 'mail not sent'})
