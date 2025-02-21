from rest_framework import serializers
from .models import Projects, Tasks, Stages

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projects
        fields = '__all__'

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tasks
        fields = '__all__'

class StageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stages
        fields = '__all__'