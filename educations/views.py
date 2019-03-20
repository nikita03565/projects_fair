from .serializers import FacultySerializer, EducationSerializer, EduProgramSerializer, UniversitySerializer
from .models import EduProgram, Education, University, Faculty
from rest_framework import generics


class FacultyList(generics.ListCreateAPIView):
    queryset = Faculty.objects.all()
    serializer_class = FacultySerializer


class FacultyDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Faculty.objects.all()
    serializer_class = FacultySerializer


class UniversityList(generics.ListCreateAPIView):
    queryset = University.objects.all()
    serializer_class = UniversitySerializer


class UniversityDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = University.objects.all()
    serializer_class = UniversitySerializer


class EducationList(generics.ListCreateAPIView):
    queryset = Education.objects.all()
    serializer_class = EducationSerializer


class EducationDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Education.objects.all()
    serializer_class = EducationSerializer


class EduProgramList(generics.ListCreateAPIView):
    queryset = EduProgram.objects.all()
    serializer_class = EduProgramSerializer


class EduProgramDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = EduProgram.objects.all()
    serializer_class = EduProgramSerializer
