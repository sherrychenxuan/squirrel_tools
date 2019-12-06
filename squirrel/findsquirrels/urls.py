from django.urls import path
from . import views

urlpatterns = [
	path('map/',views.map),
	path('map/',views.select_samples),
        path('sightings/',views.all_squirrels),
        path('sightings/add',views.add_squirrel),
]

