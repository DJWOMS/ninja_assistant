from io import BytesIO
from typing import Optional
from uuid import uuid4

import requests
from django.conf import settings

from django.contrib.auth import get_user_model
from django.core.files.base import ContentFile
from django.core.files.images import ImageFile

from src.auth import schemas


class BaseService:
    model = get_user_model()

    def __init__(self, username: str, email: str = None, avatar: str = None):
        self._user: Optional[settings.AUTH_USER_MODEL] = None
        self._email = email
        self._username = username
        self._avatar = avatar

    def _get_or_create_user(self) -> None:
        try:
            self._user = self.model.objects.get(username=self._username)
        except self.model.DoesNotExist:
            self._user = self.model.objects.create(
                username=self._username,
                email=self._email,
                avatar=self._save_avatar(self._avatar),
            )

    def _save_avatar(self, link):
        response = requests.get(link)
        return ImageFile(BytesIO(response.content), name=f'{uuid4()}.jpg')

    def authorize_user(self) -> int:
        self._get_or_create_user()
        return self._user.id


class Google(BaseService):
    def __init__(self, user: schemas.GoogleAuth):
        super().__init__(user.email.split(sep='@')[0], user.email, user.picture)
