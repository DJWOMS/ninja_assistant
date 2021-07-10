from datetime import datetime

from ninja import Schema
from src.users.schemas import UserOut


class WordBase(Schema):
    game_id: int
    word_en: str
    word_ru: str
    definition: str


class WordOut(WordBase):
    id: int
    user: UserOut
    create_at: datetime
    update_at: datetime
