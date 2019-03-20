from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from users import views
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'users', views.UserViewSet)

urlpatterns = [

]

urlpatterns += router.urls
