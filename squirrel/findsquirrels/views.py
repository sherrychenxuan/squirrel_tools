from django.shortcuts import render
from django.http import HttpResponse
from .models import Squirrel
from .forms import SquirrelForm
import json

def map(request):
	return render(request,'findsquirrels/map.html')


def select_samples(request):
	squirrels = Squirrel.objects.all()
	sightings = squirrels[0:50]
	context = {
		'sightings': sightings,
	}
	return render(request,'findsquirrels/map.html',context)

def all_squirrels(request):
    squirrels = Squirrel.objects.all()
    context = {
            'squirrels':squirrels,
    }
    return render(request,'findsquirrels/sightings.html',context)


def add_squirrel(request):
    if request.method == 'POST':
        form = SquirrelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(f'/findsquirrels/sightings')
    else:
        form = SquirrelForm()

    context = {
            'form':form,
    }

    return render(request,'sightings/add.html',context)	


def edit_squirrel(request,unique_squirrel_id):
    squirrel = Squirrel.objects.get(unique_squirrel_id=unique_squirrel_id)
    if request.method == 'POST':
        form = SquirrelForm(request.POST, instance=squirrel)
        if form.is_valid():
            form.save()
            return redirect(f'/sightings')
    else:
        form = SquirrelForm(instance=squirrel)
        #build a new empty form

    context = {
            'form':form,
    }

    return render(request,'sightings/add.html',context)
    
