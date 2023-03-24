from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Karaokê",
      default_version='v1',
      description="Uma API de Karaokê",
      terms_of_service="#",
      contact=openapi.Contact(email="#"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

from apps.music_module.views import AuthorViewSet

router = routers.DefaultRouter()

router.register('authors', AuthorViewSet, basename = 'Authors')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path(
            'doc/', schema_view.with_ui('swagger', cache_timeout=0), 
            name='karaoke-api-documentation'
        )
]
