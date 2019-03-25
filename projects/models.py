from django.db import models
from users.models import User
from datetime import date, timedelta
from django.utils.translation import ugettext_lazy as _
from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator


class Project(models.Model):
    title = models.CharField(max_length=255, help_text="Title of the project", unique=True, )
    description_short = models.TextField(max_length=1024, help_text="Brief description", )
    description_full = models.TextField(max_length=8192, help_text="Detail description", )
    num_participants = models.PositiveSmallIntegerField(help_text="Number of participants", default=5)
    date_start = models.DateField("Project start date", default=date.today,
                                  validators=[MinValueValidator(date.today()),
                                              MaxValueValidator(date.today() + timedelta(weeks=260))],
                                  )
    date_end = models.DateField("Project end date", default=date.today,
                                validators=[MinValueValidator(date.today()),
                                            MaxValueValidator(date.today() + timedelta(weeks=260))],
                                )
    date_reg_end = models.DateField("Application deadline", default=date.today,
                                    validators=[MinValueValidator(date.today()),
                                                MaxValueValidator(date.today() + timedelta(weeks=260))],
                                    )
    participants = models.ManyToManyField(settings.AUTH_USER_MODEL, through='Participation', related_name='projects', )

    PROJECT_STATUS = (
        ('m', 'Moderation'),
        ('c', 'Collecting participants'),
        ('p', 'In progress'),
        ('f', 'Finished'),
        ('r', 'Rejected'),
    )
    status = models.CharField(max_length=1, choices=PROJECT_STATUS, default='m', help_text='Project status')

    class Meta:
        ordering = ('date_start', )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return "/%i/" % self.id


class Participation(models.Model):
    ROLE_STUDENT = 'ST'
    ROLE_TEACHER = 'TE'
    ROLE_CHOICES = (
        (ROLE_STUDENT, _('Student')),
        (ROLE_TEACHER, _('Teacher'))
    )
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='participations', on_delete=models.CASCADE, )
    project = models.ForeignKey('Project', related_name='participations', on_delete=models.CASCADE, )
    role = models.CharField(max_length=2, choices=ROLE_CHOICES, default=ROLE_STUDENT, )

    class Meta:
        unique_together = ('user', 'project')
