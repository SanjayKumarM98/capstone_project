from user_friends.views import *


user_friends_api_blueprint = Blueprint('user-friends-api', __name__)


# To follow or unfollow a friend
@user_friends_api_blueprint.route('/friends', methods=['POST'])
@email_required
def follow_unfollow_controller(email, admin):
    return follow_unfollow_views(request, email, admin)
