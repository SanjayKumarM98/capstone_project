from user_feeds.views import *

user_feeds_api_blueprint = Blueprint('feeds-blueprint-api', __name__)


@user_feeds_api_blueprint.route('create_feed', methods=['POST'])
@email_required
def create_feed_controller(email):
    return create_feed_views(request, email)


@user_feeds_api_blueprint.route('show_friends_feed', methods=['GET'])
@email_required
def show_friends_feed_controller(email):
    return show_friends_feed_views(request, email)


@user_feeds_api_blueprint.route('show_public_feed', methods=['GET'])
@email_required
def show_public_feed_controller(email):
    return show_public_feed_views(request, email)
