from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=50, help_text="Tag name")

    def __str__(self):
        return self.name
