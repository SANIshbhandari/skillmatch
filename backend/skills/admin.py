from django.contrib import admin
from .models import Skill, SkillGroup, SkillSynonym


# Register your models here.
admin.site.register(SkillGroup)
admin.site.register(Skill)
admin.site.register(SkillSynonym)
