from django.contrib.auth.models import AbstractUser
from django.db import models
from educations.models import Education


class User(AbstractUser):
    bio = models.CharField(max_length=160, null=True, blank=True)
    middle_name = models.CharField(max_length=30, blank=True)
    education = models.ManyToManyField(Education, related_name="users")

    def __str__(self):
        return self.username
