from user_feeds.views import *

user_feeds_api_blueprint = Blueprint('feeds-blueprint-api', __name__)


# To create new feed
@user_feeds_api_blueprint.route('create_feed', methods=['POST'])
@email_required
def create_feed_controller(email, admin):
    return create_feed_views(request, email, admin)


# To show only friends/followers feeds
@user_feeds_api_blueprint.route('show_friends_feed', methods=['GET'])
@email_required
def show_friends_feed_controller(email, admin):
    return show_friends_feed_views(request, email, admin)


# To show all public feeds
@user_feeds_api_blueprint.route('show_public_feed', methods=['GET'])
@email_required
def show_public_feed_controller(email, admin):
    return show_public_feed_views(request, email, admin)
