from rest_framework import routers
from .views import ProjectDetail, ProjectList

from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from projects import views

urlpatterns = [
    path('projects/', views.ProjectList.as_view()),
    path('projects/<int:pk>/', views.ProjectDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
