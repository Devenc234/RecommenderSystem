from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(name):
    # print ('Hello, I am online')
    return HttpResponse('Hello from Django!')
