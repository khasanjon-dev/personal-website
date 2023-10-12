from django.shortcuts import render

from website.models import Me, About, Skills, WorkExperience, SocialMedia, Project


def home(request):
    me = Me.objects.first()
    about = About.objects.first()
    skills = Skills.objects.all()
    work_experience = WorkExperience.objects.all().order_by('-id')
    social = SocialMedia.objects.all()
    project = Project.objects.first()
    context = {
        'me': me,
        'about': about,
        'skills': skills,
        'work_experience': work_experience,
        'social': social,
        'project': project,
    }
    return render(request, 'website/index.html', context)
