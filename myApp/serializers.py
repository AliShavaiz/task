# serializers.py
from rest_framework import serializers
from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('id', 'user', 'task_name', 'created_at')

    # def create(self, validated_data):
    #     # Assign the logged-in user to the 'user' field in the Task model
    #     request = self.context.get('request')

    #     # Now you can access request data
    #     name = request.data.get('task_name')
    #     userid = request.data.get('userid')
    #     print("kkkkkkkkkkkkkkkkkkkkkkkkkkk",userid,name)
    #     validated_data['user'] = self.context['request'].user
    #     return super(TaskSerializer, self).create(validated_data)
