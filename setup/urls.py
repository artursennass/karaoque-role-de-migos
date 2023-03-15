from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from apps.music_module.views import AuthorViewSet

router = routers.DefaultRouter()

router.register('authors', AuthorViewSet, basename = 'Authors')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
