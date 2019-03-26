from django.db import models
from django.utils.translation import ugettext_lazy as _


class Skill(models.Model):
    SCI_SKILL = 'SC'
    AP_SKILL = 'AP'
    EXT_SKILL = 'EX'
    SKILL_TYPE = (
        (SCI_SKILL , _('Scientific Skill')),
        (AP_SKILL, _('Applied Skill')),
        (EXT_SKILL, _('External Skill')),
    )
    type = models.CharField(max_length=2, choices=SKILL_TYPE, default=SCI_SKILL, help_text='Skill type')

    name = models.CharField(max_length=50, help_text="Skill name")

    def __str__(self):
        return self.name
