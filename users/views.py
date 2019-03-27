from .serializers import UserSerializer
from rest_framework import generics
from .models import User
from django.shortcuts import get_object_or_404
from projects.models import Project
from projects.serializers import ProjectSerializer
import services
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import permissions
from rest_framework.views import APIView
from django.contrib.auth import login
from rest_framework.authtoken.models import Token
from .serializers import LoginSerializer


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()

    @action(detail=True, methods=['get'], permission_classes=[permissions.IsAuthenticated])
    def user_projects_as_teacher(self, request, pk):
        user = self.get_object()
        projects = services.get_courses_in_which_user_has_been_enrolled_as_teacher(user)
        serializer = ProjectSerializer(projects, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['get'], permission_classes=[permissions.IsAuthenticated])
    def user_projects_as_student(self, request, pk):
        user = self.get_object()
        projects = services.get_courses_in_which_user_has_been_enrolled_as_student(user)
        serializer = ProjectSerializer(projects, many=True)
        return Response(serializer.data)


class LoginView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]
        login(request, user)
        token, created = Token.objects.get_or_create(user=user)
        return Response({"token": token.key}, status=200)