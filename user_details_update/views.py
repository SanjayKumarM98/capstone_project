from authentication.models import *
from common.common_modules import *


def all_user_details_views(request, email):
    try:
        users = AuthenticateModels.query.all()

        all_user_details = []

        for user in users:
            if user.deleted_at is None:
                all_user_details.append({'id': user.id, 'first_name': user.first_name, 'last_name': user.last_name, 'email':user.email, 'gender':user.gender, 'dob':user.dob})

        return jsonify({'users':all_user_details})
    except Exception as e:
        print(e)
        return jsonify({'error': 'while getting list of all users record'})


def user_details_update_views(request, email):
    try:
        payload = request.form

        column_name = payload.get('field')
        value_to_be_updated = payload.get('value')

        user = AuthenticateModels.query.filter_by(email=email).first()

        if column_name == 'first_name':
            user.first_name = value_to_be_updated

        elif column_name == 'last_name':
            user.last_name = value_to_be_updated

        elif column_name == 'gender':
            user.gender = value_to_be_updated

        elif column_name == 'dob':
            user.dob = value_to_be_updated

        elif column_name == 'email':
            user.email = value_to_be_updated

        else:
            return jsonify({'message': 'Cant update the data as the field is not found in database'})

        now = datetime.now()
        updated_at = now.strftime("%d-%m-%Y %H:%M:%S")
        user.updated_at = updated_at

        if update_data(user):
            return jsonify({'message': 'user details has been updated'})

        return jsonify({'message': 'not able to update user details'})
    except Exception as e:
        print(e)
        return jsonify({'message': 'error while updating user details'})
