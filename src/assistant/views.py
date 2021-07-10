from typing import List

from asgiref.sync import sync_to_async
from ninja import Router
from .schemas import WordBase, WordOut
from .models import Word

from src.users.models import User

assistant_router = Router()


@assistant_router.post("/", response=WordOut)
async def create_word(request, payload: WordBase):
    _user = await sync_to_async(User.objects.get)(id=1)
    return await sync_to_async(Word.objects.create, thread_sensitive=True)(user=_user, **payload.dict())


@assistant_router.get("/", response=List[WordOut])
async def get_word_list(request):
    return await sync_to_async(list)(Word.objects.select_related('user').all())


@assistant_router.get("/{pk}", response=WordOut)
async def get_word(request, pk: int):
    return await sync_to_async(Word.objects.select_related('user').get)(id=pk)










