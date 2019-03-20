from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter


router = DefaultRouter()

urlpatterns = [
    path('', include(router.urls)),
    path('api/v1/', include('projects.urls')),
    path('api/v1/', include('users.urls')),
    path('api/v1/', include('educations.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('admin/', admin.site.urls),
]
