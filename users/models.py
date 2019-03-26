from django.contrib.auth.models import AbstractUser
from django.db import models

from educations.models import Education
from skills.models import Skill


class User(AbstractUser):
    bio = models.CharField(max_length=160, null=True, blank=True)
    middle_name = models.CharField(max_length=30, blank=True)
    education = models.ManyToManyField(Education, related_name="users", blank=True, )
    skills = models.ManyToManyField(Skill, related_name="Users", help_text="Skills possessed by the user", blank=True, )

    def __str__(self):
        return self.username
