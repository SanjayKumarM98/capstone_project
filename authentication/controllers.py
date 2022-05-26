from authentication.models import *
from authentication.views import *

authentication = Blueprint('authentication-api', __name__)


@authentication.route('login', methods=['POST'])
def login_controller():
    return login_views(request)


@authentication.route('signup', methods=['POST'])
def signup_controller():
    return signup_views(request)


@authentication.route('reset', methods=['PUT'])
def reset_controller():
    return reset_views(request)


@authentication.route('mail', methods=['POST'])
def reset_password_mail_controller():
    return reset_password_mail_views(request)
