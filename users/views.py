from django.contrib.auth import login
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework import status
from .serializers import LoginSerializer, UserSerializer, RegistrationSerializer
from .models import User
from projects.serializers import ProjectSerializer
from services import get_courses_in_which_user_has_been_enrolled_as_student, \
    get_courses_in_which_user_has_been_enrolled_as_teacher


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()

    @action(detail=True, methods=['get'], permission_classes=[permissions.IsAuthenticated])
    def user_projects_as_teacher(self, request, pk):
        user = self.get_object()
        projects = get_courses_in_which_user_has_been_enrolled_as_teacher(user)
        serializer = ProjectSerializer(projects, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['get'], permission_classes=[permissions.IsAuthenticated])
    def user_projects_as_student(self, request, pk):
        user = self.get_object()
        projects = get_courses_in_which_user_has_been_enrolled_as_student(user)
        serializer = ProjectSerializer(projects, many=True)
        return Response(serializer.data)


class LoginView(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key}, status=status.HTTP_200_OK)


class RegistrationView(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request):
        serializer = RegistrationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        if serializer.is_valid():
            user = serializer.save()
            if user:
                token = Token.objects.create(user=user)
                json = serializer.data
                json['token'] = token.key
                return Response(json, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ChangePasswordView(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request):
        user = get_object_or_404(User, email=request.user.email)
        user.set_password(request.data.get("new_password", ""))
        user.save()
        return Response({'detail': 'Password has been saved.'})
