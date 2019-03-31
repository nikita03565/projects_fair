from .serializers import FacultySerializer, EducationSerializer, EduProgramSerializer, UniversitySerializer
from .models import EduProgram, Education, University, Faculty
from rest_framework import viewsets
from rest_framework import permissions


class FacultyViewSet(viewsets.ModelViewSet):
    queryset = Faculty.objects.all()
    serializer_class = FacultySerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class UniversityViewSet(viewsets.ModelViewSet):
    queryset = University.objects.all()
    serializer_class = UniversitySerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class EducationViewSet(viewsets.ModelViewSet):
    queryset = Education.objects.all()
    serializer_class = EducationSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class EduProgramViewSet(viewsets.ModelViewSet):
    queryset = EduProgram.objects.all()
    serializer_class = EduProgramSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
