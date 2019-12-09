from django.db import models
#from django.contrib.gis.db.models import PointField
from django.utils.translation import gettext as _

# Create your models here.
class Squirrel(models.Model):
    x = models.DecimalField(
            decimal_places = 18,
            max_digits = 22,
            help_text = _("Longitude coordinate for squirrel sighting point"),
    )

    y = models.DecimalField(
            decimal_places = 18,
            max_digits = 22,
            help_text = _("Latitude coordinate for squirrel sighting point"),
    )

    unique_squirrel_id = models.CharField(
            help_text = _('Identification tag for each squirrel sightings'),
            max_length = 30,
            primary_key = True,
    )

   # hectare = models.CharField(
   #         help_text = _('Id tag'),
   #         max_length = 5,
   # )

    PM='PM'
    AM='AM'
    shift_choices=(
            (PM,'PM'),
            (AM,'AM'),)
    shift = models.CharField(
            help_text = _('sighting morning or afternoon'),
            max_length = 5,
            choices=shift_choices,
            blank = True,
    )

    date = models.CharField(
            help_text = _('sighting day and month'),
            max_length = 10,
            blank = True,
    )

   # hectare_squirrel_number = models.IntegerField(
   #         help_text = _('number of squirrel sightings'),
   # )

    Adult='Adult'
    Juvenile='Juvenile'
    age_choices=((Adult,'Adult'),(Juvenile,'Juvenile'))
    age = models.CharField(
            help_text = _('adult or juvenile'),
            max_length = 10,
            choices = age_choices,
            blank = True,
    )

    Gray='Gray'
    Cinnamon='Cinnamon'
    Black='Black'
    color_choices=((Gray,'Gray'), (Cinnamon,'Cinnamon'),
    (Black,'Black'))
    primary_fur_color = models.CharField(
            max_length = 20,
            help_text = _('Gray,Cinnamon or Black'),
            choices = color_choices,
            blank = True,
    )

   # highlight_fur_color = models.CharField(
   #         max_length = 10,
   # )

   # combination_of_primary_and = models.CharField(
   #         help_text = _('combination of previous two columns'),
   #         max_length = 30,
   # )

   # color_notes = models.CharField(
   #         max_length = 100,
   # )

    Ground_Plane='Ground_Plane'
    Above_Ground='Above_Ground'
    Other='Other'
    location_choices=( (Ground_Plane,'Ground_Plane'), (Above_Ground,'Above_Ground'))
    location = models.CharField(
            max_length = 20,
            help_text = _('Ground Plane or Above Ground'),
            choices = location_choices,
            blank = True,
    )

   # above_ground_sighter = models.CharField(
   #         max_length = 10,
   # )

    specific_location = models.CharField(
            max_length = 100,
            help_text = _('your commentary'),
            blank = True
    )

    running = models.BooleanField()

    chasing = models.BooleanField()

    climbing = models.BooleanField()

    eating = models.BooleanField()

    foraging = models.BooleanField()

    other_activities = models.CharField(
            max_length = 50,
            blank = True,
    )

    kuks = models.BooleanField()

    quaas = models.BooleanField()

    moans = models.BooleanField()
    
    tail_flags = models.BooleanField()

    tail_twitches = models.BooleanField()

    approaches = models.BooleanField()

    indifferent = models.BooleanField()

    runs_from = models.BooleanField()

   # other_interactions = models.CharField(
   #         max_length = 50,
   # )

   # lat_long = PointField()

   # zip_codes = models.CharField(max_length=10)

   # community_districts = models.IntegerField()

   # borough_boundaries = models.IntegerField()

   # city_council_districts = models.IntegerField()

   # police_precincts = models.IntegerField()

    def __str__(self):
        return self.unique_squirrel_id
