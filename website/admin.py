from django.contrib import admin

from website.models import Me, About, Skills, WorkExperience, SocialMedia, Project
from website.models.me import WhatIDo


@admin.register(Me)
class MeAdmin(admin.ModelAdmin):
    pass


@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    pass


@admin.register(Skills)
class SkillsAdmin(admin.ModelAdmin):
    pass


@admin.register(WorkExperience)
class WorkExperienceAdmin(admin.ModelAdmin):
    pass


@admin.register(SocialMedia)
class SocialMediaAdmin(admin.ModelAdmin):
    pass


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    pass


@admin.register(WhatIDo)
class WhatIDoAdmin(admin.ModelAdmin):
    pass
