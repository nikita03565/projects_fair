from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from educations import views as educations_views
from users import views as users_views
from projects import views as projects_views

router = DefaultRouter()

router.register(r'educations', educations_views.EducationViewSet)
router.register(r'faculties', educations_views.FacultyViewSet)
router.register(r'edu_programs', educations_views.EduProgramViewSet)
router.register(r'universities', educations_views.UniversityViewSet)
router.register(r'users', users_views.UserViewSet)
router.register(r'projects', projects_views.ProjectViewSet)

urlpatterns = [
    path('api/v1/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
    path('admin/', admin.site.urls),
]
