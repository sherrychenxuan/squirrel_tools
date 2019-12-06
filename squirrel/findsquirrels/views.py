from django.shortcuts import render
from django.http import HttpResponse
from .models import Squirrel

def map(request):
	return render(request,'findsquirrels/map.html')


    
