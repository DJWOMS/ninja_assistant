"""config URL Configuration
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from ninja import NinjaAPI

from src.assistant.views import assistant_router
from src.users.views import user_router
from src.auth.views import auth_router

api = NinjaAPI(version='0.2.0')

api.add_router("auth/", auth_router)
api.add_router("users/", user_router)
api.add_router("assistant/", assistant_router)


urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/v1/", api.urls),
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



