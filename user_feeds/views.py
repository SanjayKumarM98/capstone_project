from user_feeds.models import *
from user_friends.models import *
from common.common_modules import *


def create_feed_views(request, email):
    try:
        payload = request.json
        feeds = UserFeedsModel()

        feeds.title = payload['title']
        feeds.description = payload['description']
        feeds.image = payload['image']
        feeds.tags = payload['tags']
        feeds.category = payload['category']
        feeds.visibility = payload['visibility']
        feeds.created_by = email
        if 'detail' in payload:
            feeds.detail = payload['detail']
        print('User Feed Created')
        if add_data(feeds):
            return jsonify({'message': 'User Feed Successfully Created'})
        return jsonify({'message': 'unable to create_feed users new feed'})
    except Exception as e:
        print(e)
        return jsonify({'message': 'error while creating users new feed'})


def show_friends_feed_views(request, email):
    try:
        friends = FriendsModel.query.filter(FriendsModel.follower == email).all()
        friends_list = []
        for i in friends:
            friends_list.append(i.following)

        friends_feeds = []
        for friend in friends_list:
            friend_feed = UserFeedsModel.query.filter(UserFeedsModel.created_by == str(friend), (UserFeedsModel.visibility == 'public') | (UserFeedsModel.visibility == 'friends')).all()
            for feed in friend_feed:
                friends_feeds.append({'title': feed.title, 'description': feed.description, 'image': feed.image, 'detail': feed.detail, 'tags': feed.tags, 'category': feed.category})
        return jsonify({'feeds': friends_feeds})

    except Exception as e:
        print('error', e)
        return jsonify({'error': 'in show friends feeds!!!!'})


def show_public_feed_views(request, email):
    try:
        user = UserFeedsModel.query.filter(UserFeedsModel.visibility == 'public').all()
        public_feeds = []
        for feed in user:
            public_feeds.append({'title': feed.title, 'description': feed.description, 'image': feed.image, 'detail': feed.detail, 'tags': feed.tags, 'category': feed.category})
        return jsonify({'feeds': public_feeds})

    except Exception as e:
        print(e)
        return jsonify({'error': 'in show public feeds!!!'})
