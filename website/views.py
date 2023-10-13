from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import render, redirect

from root.settings import MY_EMAIL
from website.forms import MessageForm
from website.models import Me, About, Skills, WorkExperience, SocialMedia, Project


def home(request):
    me = Me.objects.first()
    about = About.objects.first()
    skills = Skills.objects.all()
    work_experience = WorkExperience.objects.all().order_by('-id')
    social = SocialMedia.objects.all()
    projects = Project.objects.all().order_by('-id')
    context = {
        'me': me,
        'about': about,
        'skills': skills,
        'work_experience': work_experience,
        'social': social,
        'projects': projects,
    }
    return render(request, 'website/index.html', context)


def send_email_message(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            email = form.data.get('email')
            message = form.data.get('message')
            first_name = form.data.get('first_name')
            send_email(request, first_name, message, email)

        return redirect('home')


def send_email(request, email: str, first_name: str, message: str):
    send_mail(f'Your Website: Message from {first_name}', message, email, [MY_EMAIL], fail_silently=False)
