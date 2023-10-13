from django.urls import path

from website.views import home, send_email_message

urlpatterns = [
    path('', home, name='home'),
    path('send-email', send_email_message, name='send-email')
]
