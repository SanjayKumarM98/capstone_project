from user_details_update.views import *

user_details_update_blueprint = Blueprint('user-details-update-api', __name__)


@user_details_update_blueprint.route('all', methods=['GET'])
@email_required
def all_user_details_controller(email):
    return all_user_details_views(request, email)


@user_details_update_blueprint.route('update', methods=['PUT'])
@email_required
def user_details_update_controller(email):
    return user_details_update_views(request, email)
