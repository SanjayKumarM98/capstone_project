from authentication.controllers import *
from user_feeds.controllers import *
from user_details_update.controllers import *
from user_friends.controllers import *

app.register_blueprint(authentication, name='url_one', url_prefix='/api/v1/authentication/')
app.register_blueprint(user_feeds_api_blueprint, name='user_feeds_url_one', url_prefix='/api/v1/user-feeds/')
app.register_blueprint(user_details_update_blueprint, name='user_details_update_url_one', url_prefix='/api/v1/user/')
app.register_blueprint(user_friends_api_blueprint, name='user_friends_url_one', url_prefix='/api/v1/network/')

if __name__ == '__main__':
    app.run(debug=True)

