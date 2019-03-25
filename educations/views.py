from .serializers import FacultySerializer, EducationSerializer, EduProgramSerializer, UniversitySerializer
from .models import EduProgram, Education, University, Faculty
from rest_framework import viewsets


class FacultyViewSet(viewsets.ModelViewSet):
    queryset = Faculty.objects.all()
    serializer_class = FacultySerializer


class UniversityViewSet(viewsets.ModelViewSet):
    queryset = University.objects.all()
    serializer_class = UniversitySerializer


class EducationViewSet(viewsets.ModelViewSet):
    queryset = Education.objects.all()
    serializer_class = EducationSerializer


class EduProgramViewSet(viewsets.ModelViewSet):
    queryset = EduProgram.objects.all()
    serializer_class = EduProgramSerializer

