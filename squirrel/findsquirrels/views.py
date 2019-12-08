from django.shortcuts import render
from django.http import HttpResponse
from .models import Squirrel
from .forms import SquirrelForm

def stats(request):
        return render(request,'sightings/stats.html')

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
            return HttpResponse(f'Updated squirrel {unique_squirrel_id}')
    else:
        form = SquirrelForm(instance=squirrel)

    context = {
            'form':form,
    }

    return render(request,'sightings/add.html',context)

def stats(request):
<<<<<<< HEAD
   return render(request,'sightings/stats.html')

=======
    return render(request,'sightings/stats.html')
>>>>>>> 03c65563dd9c6df37850b269fdec77eb5ae7a784
