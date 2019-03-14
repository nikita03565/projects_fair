from django.db import models
from django.contrib.auth.models import User
from datetime import date


class Project(models.Model):
    name = models.TextField(max_length=255, help_text="Название проекта", )
    lead = models.ForeignKey(User, related_name="projects_lead", help_text="Руководитель", on_delete=models.CASCADE, )
    description_short = models.TextField(max_length=1024, help_text="Краткое описание проекта", )
    description_full = models.TextField(max_length=8192, help_text="Подробное описание проекта", )
    num_participants = models.PositiveSmallIntegerField(help_text="Количество участников", default=5)
    date_start = models.DateField("Дата начала проекта", default=date.today)
    date_end = models.DateField("Дата окончания проекта", default=date.today)
    date_reg_end = models.DateField("Дата окончания приема заявок", default=date.today)

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
        return self.name

    def get_absolute_url(self):
        return "/%i/" % self.id
