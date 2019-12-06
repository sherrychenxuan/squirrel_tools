from django.shortcuts import render
from django.http import HttpResponse
from .models import Squirrel

def map(request):
	return render(request,'findsquirrels/map.html')


def getlocation(request):
	squirrels = Squirrel.objects.values_list("unique_squirrel_id","y","x")
	sample=squirrels.sample(1)
	context = {
		'id': sample.unqunique_squirrel_id
		'y':sample.y
		'x':sample.x 
	}
	return render(request,'findsquirrels/map.html',context)
	
    
