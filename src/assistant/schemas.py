from datetime import datetime

from ninja import Schema
from src.users.schemas import UserOut


class Game(Schema):
    name: str


class GameOut(Game):
    id: int


class WordBase(Schema):
    word_en: str
    word_ru: str
    definition: str


class WordCreate(WordBase):
    game_id: int


class WordOut(WordBase):
    id: int
    game: Game
    definition: str = None


class WordSingleOut(WordBase):
    id: int
    game: Game
    user: UserOut
    create_at: datetime
    update_at: datetime


class Filters(Schema):
    word_en: str = None
    word_ru: str = None
    game_id: int = None


class CorrectionBase(Schema):
    word_id: int
    definition: str
    # image


class CorrectionOut(CorrectionBase):
    id: int
    word: WordOut


class CorrectionSingleOut(CorrectionBase):
    id: int
    word: WordSingleOut













