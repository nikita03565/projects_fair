from rest_framework import serializers
from .models import EduProgram, Education, University, Faculty


class UniversitySerializer(serializers.ModelSerializer):
    class Meta:
        model = University
        fields = "__all__"


class FacultySerializer(serializers.ModelSerializer):
    class Meta:
        model = Faculty
        fields = "__all__"


class EduProgramSerializer(serializers.ModelSerializer):
    class Meta:
        model = EduProgram
        fields = "__all__"


class EducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Education
        fields = "__all__"
