from rest_framework import serializers
from .models import Project


class ProjectListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('id', 'title', 'description_short', 'num_participants', 'date_start',
                  'date_end', 'date_reg_end', 'status')


class ProjectDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('id', 'title', 'participants', 'description_short', 'description_full', 'num_participants',
                  'date_start', 'date_end', 'date_reg_end', 'status')
