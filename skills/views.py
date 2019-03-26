from .models import Skill
from .serializers import SkillSerializer
from rest_framework import viewsets
from rest_framework import permissions


class SkillViewSet(viewsets.ModelViewSet):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )
