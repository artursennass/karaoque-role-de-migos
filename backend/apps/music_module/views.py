from rest_framework import viewsets

from apps.music_module.models import Author
from apps.music_module.serializer import AuthorSerializer

class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer