from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('universities/', views.UniversityList.as_view()),
    path('universities/<int:pk>/', views.UniversityDetail.as_view()),
    path('faculties/', views.FacultyList.as_view()),
    path('faculties/<int:pk>/', views.FacultyDetail.as_view()),
    path('edu_programs/', views.EduProgramList.as_view()),
    path('edu_programs/<int:pk>/', views.EduProgramDetail.as_view()),
    path('educations/', views.EducationList.as_view()),
    path('educations/<int:pk>/', views.EducationDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
