from django.core.exceptions import PermissionDenied
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.decorators import action

from .models import Project, Participation
from .serializers import ProjectSerializer, ParticipationSerializer
from users.serializers import UserSerializer
from services import get_project_teachers, get_project_students


class IsTeacherOrReadOnly(permissions.BasePermission):
    """
    Object-level permission to only allow owners of an object to edit it.
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        return request.user in get_project_teachers(obj)


class IsTeacher(permissions.BasePermission):
    """
    Object-level permission to only allow owners of an object to edit it.
    """

    def has_object_permission(self, request, view, obj):
        return request.user in get_project_teachers(obj)


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsTeacherOrReadOnly)

    @action(detail=True, methods=['get'], permission_classes=[permissions.IsAuthenticated])
    def get_project_teachers(self, request, pk=None):
        project = self.get_object()
        users = get_project_teachers(project)
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['get'], permission_classes=[permissions.IsAuthenticated, IsTeacher])
    def get_project_students(self, request, pk=None):
        project = self.get_object()
        users = get_project_students(project)
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['get'], permission_classes=[permissions.IsAuthenticated])
    def enroll_as_student(self, request, pk=None):
        project = self.get_object()
        user = request.user
        participation, created = Participation.objects.get_or_create(
                project=project,
                user=user,
                defaults={'role': Participation.ROLE_STUDENT}
            )
        if not created:
            if participation.role == Participation.ROLE_TEACHER:
                raise PermissionDenied('Already the teacher. Cannot enroll.')
            else:
                raise PermissionDenied('Already enrolled. Cannot re-enroll.')
        serializer = ParticipationSerializer(participation, many=False)
        return Response(serializer.data)

    @action(detail=True, methods=['get'], permission_classes=[permissions.IsAuthenticated])
    def enroll_as_teacher(self, request, pk=None):
        project = self.get_object()
        user = request.user
        participation, created = Participation.objects.get_or_create(
            project=project,
            user=user,
            defaults={'role': Participation.ROLE_TEACHER}
        )
        if not created:
            if participation.role == Participation.ROLE_STUDENT:
                raise PermissionDenied('Already the student. Cannot enroll.')
            else:
                raise PermissionDenied('Already enrolled. Cannot re-enroll.')
        serializer = ParticipationSerializer(participation, many=False)
        return Response(serializer.data)
