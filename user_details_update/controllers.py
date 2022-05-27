from user_details_update.views import *

user_details_update_blueprint = Blueprint('user-details-update-api', __name__)


# The below route lists all the users present currently
@user_details_update_blueprint.route('all', methods=['GET'])
@email_required
def all_user_details_controller(email, admin):
    return all_user_details_views(request, email, admin)


# The below route is used to update any particular field value
@user_details_update_blueprint.route('update', methods=['PUT'])
@email_required
def user_details_update_controller(email, admin):
    return user_details_update_views(request, email, admin)
