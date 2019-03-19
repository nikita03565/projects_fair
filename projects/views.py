from .models import Project
from .serializers import ProjectListSerializer, ProjectDetailSerializer
from rest_framework import generics
from rest_framework import permissions


class ProjectList(generics.ListCreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectListSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )


class ProjectDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectDetailSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )
