import jwt

from common.init import *


@app.before_request
def before_request_func():
    if request.endpoint == 'login' or request.endpoint == 'signup' or request.endpoint == 'reset' or request.endpoint == 'mail':
        return None
    else:
        token = None
        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token']
        # return 401 if token is not passed
        if not token:
            return jsonify({'message': 'Token is missing !!!'}), 401

        try:
            # decoding the payload to fetch the stored details
            data = jwt.decode(token, app.config['SECRET_KEY'], algorithms=["HS256"])
            if data:
                exp = data['exp']
                ct = datetime.utcnow().strftime('%Y%m%d%H%M%S')
                FMT = '%Y%m%d%H%M%S'
                tdelta = (datetime.strptime(exp, FMT) - datetime.strptime(ct, FMT)).seconds
                min = tdelta / 60

                if float(min) <= float(min_time):
                    return jsonify({'message': 'Token has expired!!'}), 401

            else:
                return jsonify({'message': 'Please Pass Token For Validation!!!!'})
        except Exception as e:
            print(e)
            return jsonify({'message': 'Token Is Incorrect!!!'}), 401


def add_data(obj):
    try:
        db.session.add(obj)
        db.session.commit()
        return obj
    except Exception as e:
        print("add_data", e)
        return None


def update_data(obj):
    try:
        db.session.commit()
        return obj
    except Exception as e:
        print("update_data", e)
        return None


def delete_data(obj):
    try:
        now = datetime.now()
        obj.deleted_at = now.strftime("%d-%m-%Y %H:%M:%S")
        db.session.commit()
        return obj
    except Exception as e:
        print("delete_data", e)
        return None


# decorator function to decode email from jwt token.
def email_required(func):
    @wraps(func)
    def decode_email(*args, **kwargs):
        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token']
            token_decode = jwt.decode(token, app.config['SECRET_KEY'], algorithms=["HS256"])
            if token_decode:
                kwargs['email'], kwargs['admin'] = token_decode['email'], token_decode['admin']
                return func(*args, **kwargs)
            else:
                return jsonify({'message': 'token is expired!!!'})
        else:
            return jsonify({'message': 'token not passed!!!'})
    return decode_email
