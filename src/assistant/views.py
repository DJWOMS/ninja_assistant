from typing import List

from ninja import Router, Query
from ninja.errors import HttpError

from . import schemas
from .models import Word, Correction, Game

from ..auth.services.jwt_service import AuthBearer


assistant_router = Router(tags=['assistant'])


@assistant_router.get("/game", response=List[schemas.GameOut])
def get_game_list(request):
    return Game.objects.all()


@assistant_router.post("/word", response=schemas.WordOut, auth=AuthBearer())
def create_word(request, payload: schemas.WordCreate):
    return Word.objects.create(user=request.auth, **payload.dict())


@assistant_router.get("/word", response=List[schemas.WordOut])
def get_word_list(request, filters: schemas.Filters = Query(...)):
    return Word.objects.select_related('user', 'game').filter(**filters.dict(exclude_none=True))


@assistant_router.get("/word/{pk}", response=schemas.WordSingleOut)
def get_word(request, pk: int):
    return Word.objects.select_related('user', 'game').get(id=pk)


@assistant_router.post("/correction", response=schemas.CorrectionOut, auth=AuthBearer())
def create_correction(request, payload: schemas.CorrectionBase):
    return Correction.objects.create(user=request.auth, **payload.dict())


@assistant_router.get("/correction", response=List[schemas.CorrectionOut], auth=AuthBearer())
def get_correction_list(request):
    return Correction.objects.select_related('word').filter(user=request.auth)


@assistant_router.get("/correction/{pk}", response=schemas.CorrectionSingleOut, auth=AuthBearer())
def get_correction(request, pk: int):
    return Correction.objects.select_related('user', 'word').get(user=request.auth, id=pk)


@assistant_router.delete("/correction/{pk}", auth=AuthBearer())
def delete_correction(request, pk: int):
    try:
        correction = Correction.objects.get(user=request.auth, id=pk)
    except Correction.DoesNotExist:
        raise HttpError(404, "Not found")
    correction.delete()
    return {}
















