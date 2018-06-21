from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.conf import settings

def home(request):
	context = {}
	template = 'home.html'
	return render(request,template,context)

def about(request):
	context = {}
	template = 'about.html'
	return render(request,template,context)

def fruits(request):
	context = {}
	template = 'fruits.html'
	return render(request,template,context)

def animals(request):
	context = {}
	template = 'animals.html'
	return render(request,template,context)

def flowers(request):
	context = {}
	template = 'flowers.html'
	return render(request,template,context)

@login_required
def userProfile(request):
	user = request.user
	context = {'user':user}
	template = 'profile.html'
	return render(request,template,context)