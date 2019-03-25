from rest_framework import serializers
from .models import EduProgram, Education, University, Faculty


class UniversitySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = University
        fields = "__all__"


class FacultySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Faculty
        fields = "__all__"


class EduProgramSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = EduProgram
        fields = "__all__"


class EducationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Education
        fields = "__all__"
