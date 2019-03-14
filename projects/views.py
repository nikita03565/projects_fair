from rest_framework import viewsets
from .models import Project
from .serializers import ProjectListSerializer, ProjectDetailSerializer
from rest_framework import generics


class ProjectList(generics.ListCreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectListSerializer


class ProjectDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectDetailSerializer
