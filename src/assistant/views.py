from typing import List

from asgiref.sync import sync_to_async
from ninja import Router
from .schemas import WordBase, WordOut
from .models import Word

from ..auth.services.jwt_service import AuthBearer

assistant_router = Router(tags=['assistant'])


@assistant_router.post("/", response=WordOut, auth=AuthBearer())
def create_word(request, payload: WordBase):
    # print('view', request.auth)
    return Word.objects.create(user=request.auth, **payload.dict())


@assistant_router.get("/", response=List[WordOut])
async def get_word_list(request):
    return await sync_to_async(list)(Word.objects.select_related('user').all())


@assistant_router.get("/{pk}", response=WordOut)
async def get_word(request, pk: int):
    return await sync_to_async(Word.objects.select_related('user').get)(id=pk)










