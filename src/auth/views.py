from django.shortcuts import render
from django.views.generic.base import View
from ninja import Router
from . import schemas
from .services import google


auth_router = Router()


@auth_router.get("/")
def google_login(request):
    return render(request, 'auth/index.html')


@auth_router.post("/google", response=schemas.Token)
def auth_google(request, user: schemas.GoogleAuth):
    user_id, token = google.google_auth(user)
    return schemas.Token(id=user_id, token=token.get("access_token"))
