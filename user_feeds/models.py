from authentication.models import *


class UserFeedsModel(BaseModel):

    __tablename__ = 'feeds'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(1000), nullable=False)
    description = db.Column(db.Text)
    image = db.Column(db.String(1000))
    detail = db.Column(db.Text)
    tags = db.Column(db.String(50))
    category = db.Column(db.String(50))
    visibility = db.Column(db.String(100), default='Friends')
    created_by = db.Column(db.String(100), db.ForeignKey(AuthenticateModels.email))
