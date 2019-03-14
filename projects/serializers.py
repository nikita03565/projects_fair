from rest_framework import serializers
from .models import Project
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    projects = serializers.PrimaryKeyRelatedField(many=True, queryset=Project.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'projects')


class ProjectListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('id', 'name', 'lead', 'description_short', 'num_participants', 'date_start',
                  'date_end', 'date_reg_end', 'status')


class ProjectDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('id', 'name', 'lead', 'description_short', 'description_full', 'num_participants', 'date_start',
                  'date_end', 'date_reg_end', 'status')