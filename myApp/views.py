from django.shortcuts import render

# Create your views here.


# views.py
from .models import Task
from .serializers import TaskSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .task import print_task_name
# from SelteqTask.celery import add

class TaskList(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, format=None):
        snippets = Task.objects.all()
        serializer = TaskSerializer(snippets, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            task = serializer.save()
            b = print_task_name.delay(task.task_name)
            print(f'Name : {b}')
            response_data = {
            "task_name": task.task_name,
            "created_at": task.created_at,
            "user": task.user.username 
        }
            return Response(response_data, status=status.HTTP_201_CREATED)
            # return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)