from .models import Tag
from .serializers import TagSerializer
from rest_framework import viewsets
from rest_framework import permissions


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )
