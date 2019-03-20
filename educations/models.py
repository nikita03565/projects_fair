from django.db import models
from datetime import date
from django.utils.translation import ugettext_lazy as _
from django.core.validators import MaxValueValidator, MinValueValidator


class University(models.Model):
    name = models.CharField(max_length=255, help_text="University name",)

    class Meta:
        verbose_name_plural = "Universities"

    def __str__(self):
        return self.name


class EduProgram(models.Model):
    name = models.CharField(max_length=255, help_text="Educational program name")

    def __str__(self):
        return self.name


class Faculty(models.Model):
    name = models.CharField(max_length=255, help_text="Faculty name")

    class Meta:
        verbose_name_plural = "Faculties"

    def __str__(self):
        return self.name


class Education(models.Model):
    BACHELOR_STAGE = 'B'
    MASTER_STAGE = 'M'
    GRADUATE_STUDENT_STAGE = 'G'
    STAGE_CHOICES = (
        (BACHELOR_STAGE, _('Bachelor')),
        (MASTER_STAGE, _('Master')),
        (GRADUATE_STUDENT_STAGE, _('Graduate Student')),
    )
    edu = models.ForeignKey(University,  on_delete=models.CASCADE,   related_name='education')
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE,   related_name='education')
    prog = models.ForeignKey(EduProgram, on_delete=models.CASCADE,   related_name='education')
    stage = models.CharField(max_length=1, choices=STAGE_CHOICES, default=BACHELOR_STAGE, )
    enroll_year = models.PositiveIntegerField(help_text="Enroll year",
                                              validators=[MinValueValidator(1984),
                                                          MaxValueValidator(date.today().year)],
                                              )
    graduation_year = models.PositiveIntegerField(help_text="Graduation year",
                                                  validators=[MinValueValidator(1984),
                                                              MaxValueValidator(date.today().year + 5)],
                                                  )

    def __str__(self):
        return str(self.edu.__str__() + " " + self.prog.__str__() + " " + self.enroll_year.__str__() + " " +
                   self.graduation_year.__str__())
