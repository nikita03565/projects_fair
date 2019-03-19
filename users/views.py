from .serializers import UserSerializer
from rest_framework import generics
from .models import User
from django.shortcuts import get_object_or_404, render
from projects.models import Project
import services


class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


def user_projects_as_teacher(request, user):
    projects = services.get_courses_in_which_user_has_been_enrolled_as_teacher(user)
    return render(request, 'projects_as_teacher.html', {
        'projects': projects,
    })


def user_projects_as_student(request, user):
    projects = services.get_courses_in_which_user_has_been_enrolled_as_student(user)
    return render(request, 'projects_as_student.html', {
        'projects': projects,
    })
