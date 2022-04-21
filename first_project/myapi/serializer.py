from dataclasses import field, fields
from rest_framework import serializers

# importing models
from todo.models import Task

class TaskSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Task
        fields = ['id','first']