from typing import List

from asgiref.sync import sync_to_async
from ninja import Router

from src.users.models import User
from src.users.schemas import UserOut


user_router = Router(tags=['user'])


@user_router.get("/", response=List[UserOut])
async def get_user_list(request):
    return await sync_to_async(list)(User.objects.all())
