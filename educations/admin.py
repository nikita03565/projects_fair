from django.contrib import admin
from .models import EduProgram, Education, University, Faculty


admin.site.register(EduProgram)
admin.site.register(University)
admin.site.register(Faculty)
admin.site.register(Education)
# Register your models here.
