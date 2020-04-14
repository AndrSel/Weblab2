from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from django import template

def home(request):
	return render(request, 'templates/index.html')

def hello1(request):
	return HttpResponse(u'Hello,world1!',
content_type="text/plain")

def hello2(request):
	return HttpResponse(u'Hello,world2!')
# Create your views here.
