from ninja.errors import HttpError

from . import jwt_service
from src.users import service
from config.settings import GOOGLE_CLIENT_ID
from google.oauth2 import id_token
from google.auth.transport import requests

from .. import schemas


def google_auth(user: schemas.GoogleAuth) -> tuple:
    try:
        idinfo = id_token.verify_oauth2_token(user.token, requests.Request(), GOOGLE_CLIENT_ID)
    except ValueError:
        raise HttpError(403, "Bad code")

    user_id = service.Google(user).authorize_user()
    internal_token = jwt_service.create_token(user_id)
    return user_id, internal_token
