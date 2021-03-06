from django.contrib import admin
from django.urls import path, re_path, include
from rest_framework.routers import DefaultRouter
from educations import views as educations_views
from users import views as users_views
from projects import views as projects_views
from tags import views as tags_views
from skills import views as skills_views
from rest_framework import permissions
from users.views import LoginView, RegistrationView, ChangePasswordView, LogoutView
from drf_yasg.views import get_schema_view
from drf_yasg import openapi



schema_view = get_schema_view(
   openapi.Info(
      title="Projects Fair API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

router = DefaultRouter()

router.register(r'educations', educations_views.EducationViewSet)
router.register(r'faculties', educations_views.FacultyViewSet)
router.register(r'edu_programs', educations_views.EduProgramViewSet)
router.register(r'universities', educations_views.UniversityViewSet)
router.register(r'users', users_views.UserViewSet)
router.register(r'projects', projects_views.ProjectViewSet)
router.register(r'skills', skills_views.SkillViewSet)
router.register(r'tags', tags_views.TagViewSet)

urlpatterns = [
    path('api/v1/', include(router.urls)),
    path('api/v1/signin/', LoginView.as_view(), name='signin'),
    path('api/v1/signup/', RegistrationView.as_view(), name='signup'),
    path('api/v1/signout/', LogoutView.as_view(), name='signout'),
    path('api/v1/password_change/', ChangePasswordView.as_view(), name='password-change'),
    path('admin/', admin.site.urls),
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
