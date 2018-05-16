from django.contrib.auth.models import User
from rest_framework.response import Response
import email

def username_present(username):
    if User.objects.filter(username=username).exists():
        return Response("username is already exist")
    return False

def email_present(username):
    if User.objects.filter(email=email).exists():
        return Response("email is already exist")    
    return False
