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
    SPECIALTY_STAGE = 'S'
    MASTER_STAGE = 'M'
    GRADUATE_STUDENT_STAGE = 'G'
    STAGE_CHOICES = (
        (BACHELOR_STAGE, _('Bachelor')),
        (MASTER_STAGE, _('Master')),
        (SPECIALTY_STAGE, _('Specialist')),
        (GRADUATE_STUDENT_STAGE, _('Graduate Student')),
    )
    university = models.ForeignKey(University,  on_delete=models.CASCADE,   related_name='education')
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE,   related_name='education')
    eduProgram = models.ForeignKey(EduProgram, on_delete=models.CASCADE,   related_name='education')
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
        return str(self.university.__str__() + " " + self.faculty.__str__() +" " + self.eduProgram.__str__() + " " +
                   self.enroll_year.__str__() + " " + self.graduation_year.__str__())
