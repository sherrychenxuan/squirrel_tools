from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Squirrel
from .forms import SquirrelForm
def stats(request):
    sightings_total = Squirrel.objects.count()
    sightings_adult = Squirrel.objects.filter(age='Adult').count()
    sightings_juvenile = Squirrel.objects.filter(age='Juvenile').count()
    percent_adult = round(sightings_adult/sightings_total * 100)    
    percent_juvenile = round(sightings_juvenile/sightings_total * 100)

    black = Squirrel.objects.filter(primary_fur_color='Black').count() 
    cinnamon = Squirrel.objects.filter(primary_fur_color='Cinnamon').count()    
    gray = Squirrel.objects.filter(primary_fur_color='Gray').count()

    running_true = Squirrel.objects.filter(running=True).count()
    running_false = Squirrel.objects.filter(running=False).count()

    chasing_true = Squirrel.objects.filter(chasing=True).count()
    chasing_false = Squirrel.objects.filter(chasing=False).count()

    climbing_true = Squirrel.objects.filter(climbing=True).count()
    climbing_false = Squirrel.objects.filter(climbing=False).count()    
    eating_true = Squirrel.objects.filter(eating=True).count()
    eating_false = Squirrel.objects.filter(eating=False).count()

    foraging_true = Squirrel.objects.filter(foraging=True).count()
    foraging_false = Squirrel.objects.filter(foraging=False).count()    

    am = Squirrel.objects.filter(shift='AM').count()
    pm = Squirrel.objects.filter(shift='PM').count()
    context = {
                'sightings_total': sightings_total,
                'sightings_adult': sightings_adult,
                'sightings_juvenile': sightings_juvenile,
                'percent_adult': percent_adult,
                'percent_juvenile': percent_juvenile,
		'black':black,
		'cinnamon':cinnamon,
		'gray':gray,	
                'running': running_true,
                'chasing': chasing_true,
                'climbing': climbing_true,
		'eating': eating_true,
                'foraging': foraging_true,
		'am':am,
		'pm':pm,
            }
    return render(request, 'sightings/stats.html', context)



def select_samples(request):	
	squirrels = Squirrel.objects.all()
	sightings = squirrels[0:100]
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
            text_response = f'''
            <!doctype html>
            <html>
            Added squirrel Successfully. <a href = '/sightings'>Go back to sightings</a>
            </html>
            '''
            return HttpResponse(text_response)
           # return redirect(f'/sightings')
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
            text_response = f'''
            <!doctype html>
            <html>
            Updated squirrel {unique_squirrel_id}. <a href = '/sightings'>Go back to sightings</a>
            </html>
            '''
            return HttpResponse(text_response)
    else:
        form = SquirrelForm(instance=squirrel)

    context = {
            'form':form,
    }

    return render(request,'sightings/add.html',context)


