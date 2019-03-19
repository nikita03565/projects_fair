from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    bio = models.CharField(max_length=160, null=True, blank=True)
    middle_name = models.CharField(help_text='Отчество', max_length=30, blank=True)

    def __str__(self):
        return self.username
