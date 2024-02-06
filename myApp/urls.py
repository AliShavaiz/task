from django.urls import path
from .views import  TaskList
from . import views


urlpatterns = [
    path('task', views.TaskList.as_view()),

]
