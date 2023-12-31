from django.shortcuts import render

from website.models import Me, About, Skills, WorkExperience, SocialMedia, Project
from website.models.me import WhatIDo


def home(request):
    me = Me.objects.first()
    about = About.objects.first()
    skills = Skills.objects.all()
    work_experience = WorkExperience.objects.all().order_by('-id')
    social = SocialMedia.objects.all()
    projects = Project.objects.all().order_by('-id')
    what_do = WhatIDo.objects.all().order_by('-id')
    context = {
        'me': me,
        'about': about,
        'skills': skills,
        'work_experience': work_experience,
        'social': social,
        'projects': projects,
        'what_do': what_do
    }
    return render(request, 'website/index.html', context)
