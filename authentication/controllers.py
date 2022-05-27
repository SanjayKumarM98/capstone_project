from authentication.models import *
from authentication.views import *

authentication = Blueprint('authentication-api', __name__)


# Login Route
@authentication.route('login', methods=['POST'])
def login_controller():
    return login_views(request)


# Logout Route
@authentication.route('logout', methods=['POST'])
def logout_controller():
    return logout_views(request)


# Signup Route
@authentication.route('signup', methods=['POST'])
def signup_controller():
    return signup_views(request)


# Sending Mail For Password Reset Route
@authentication.route('mail', methods=['POST'])
def reset_password_mail_controller():
    return reset_password_mail_views(request)


# Password Reset Route
@authentication.route('reset', methods=['PUT'])
def reset_controller():
    return reset_views(request)
