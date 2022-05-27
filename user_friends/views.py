from user_friends.models import *
from common.common_modules import *


def follow_unfollow_views(request, email, admin):
    try:
        payload = request.json

        # check whether the follower email is already following or not
        user = FriendsModel.query.filter(FriendsModel.follower == email, FriendsModel.following == payload['following']).first()

        if payload['follow'] is True:
            if user is not None:
                if user.deleted_at is None:
                    return jsonify({'message': 'Already Been Followed!!!!'})
                else:
                    user.deleted_at = None
                    if add_data(user):
                        return jsonify({'message': 'Successfully followed!!!!!'})
                    return jsonify({'error': 'something went wrong!!!!'})

            user_follow = FriendsModel()
            user_follow.follower = email

            # check whether following email is present in db
            user_following = AuthenticateModels.query.filter_by(email=payload['following']).first()

            if user_following is not None:
                user_follow.following = payload['following']
            else:
                return jsonify({'error': 'user not found!!'})

            if add_data(user_follow):
                return jsonify({'message': 'Successfully followed'})
            return jsonify({'Error': 'Not able to add follow data'})

        elif payload['follow'] is False:
            if user is not None:
                if delete_data(user):
                    return jsonify({'message': 'Successfully unfollowed'})
                return jsonify({'error': 'something went wrong in unfollow step!!'})
            return jsonify({'message': 'no such record found in db'})

        else:
            return jsonify({'error': 'follow param is not passed'})

    except Exception as e:
        print('Follow_Unfollow', e)
        return jsonify({'error': 'Error found in follow unfollow module'})
