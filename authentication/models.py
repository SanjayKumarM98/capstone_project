from common.models import *


class AuthenticateModels(BaseModel):

    __tablename__ = 'authenticate'

    id = db.Column(db.String(80), default=str(uuid.uuid4()), primary_key=True)
    first_name = db.Column(db.String(40), nullable=False)
    last_name = db.Column(db.String(40), default=None, nullable=True)
    email = db.Column(db.String(50), nullable=False, unique=True)
    password = db.Column(db.String(300))
    gender = db.Column(db.String(10), nullable=False)
    dob = db.Column(db.String(20), nullable=False)
    forgot_code = db.Column(db.String(20), nullable=True)
    admin = db.Column(db.Boolean, default=False)
