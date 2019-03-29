from django.contrib.auth.models import (AbstractUser, BaseUserManager)
from django.db import models
from educations.models import Education
from skills.models import Skill


class CustomUserManager(BaseUserManager):

    def create_user_by_email(self, email, password, first_name, last_name, **extra_fields):
        if not email:
            raise ValueError('The Email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.first_name = first_name
        user.last_name = last_name
        user.save()
        return user

    def create_user(self, username, password, email=None, **extra_fields):
        if not username:
            raise ValueError('The username must be set')

        user = self.model(username=username, **extra_fields)
        email = self.normalize_email(email)
        user.set_password(password)
        user.email = email
        user.save()
        return user

    def create_superuser_by_email(self, email, password, first_name, last_name, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        return self.create_user_by_email(email, password, first_name, last_name, **extra_fields)


class User(AbstractUser):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    username = models.CharField(max_length=255, unique=False)
    bio = models.CharField(max_length=160, null=True, blank=True)
    middle_name = models.CharField(max_length=30, blank=True)
    education = models.ManyToManyField(Education, related_name="users", blank=True, )
    skills = models.ManyToManyField(Skill, related_name="Users", help_text="Skills possessed by the user", blank=True, )
    objects = CustomUserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.username


