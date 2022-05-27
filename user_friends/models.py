from authentication.models import *


class FriendsModel(BaseModel):

    __tablename__ = 'friends'

    user_follow_id = db.Column(db.Integer,primary_key=True)
    follower = db.Column(db.String(80), db.ForeignKey(AuthenticateModels.email))
    following = db.Column(db.String(80), db.ForeignKey(AuthenticateModels.email))
