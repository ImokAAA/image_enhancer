from django.shortcuts import render
from django.http import HttpResponse


def home(request):
	return render(request, 'main_page/home.html')

def about(request):
	return render(request, 'main_page/about.html')