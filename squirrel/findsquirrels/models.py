from django.db import models
from django.utils.translation import gettext as _

# Create your models here.
class Squirrel(models.Model):
    x = modelmodels.DecimalField(
            decimal_places = 18,
            max_digits = 22,
            help_text = _("Longitude coordinate for squirrel sighting point"),
    )

    y = models.DecimalField(
            decimal_places = 18,
            max_digits = 22,
            help_text = _("Longitude coordinate for squirrel sighting point"),
    )

    unique_squirrel_id = models.CharField(
            help_text = _('Identification tag for each squirrel sightings'),
            max_length = 30,
    )

    hectare = models.CharField(
            help_text = _('Id tag'),
            max_length = 5,
    )

    shift = models.CharField(
            help_text = _('sighting morning or afternoon'),
            max_length = 5,
    )

    date = models.CharField(
            help_text = _('sighting day and month'),
            max_length = 5,
    )

    hectare_squirrel_number = models.IntegerField(
            help_text = _('number of squirrel sightings'),
    )

    age = models.CharField(
            help_text = _('adult or juvenile'),
            max_length = 10,
    )

    primary_fur_color = models.CharField(
            max_length = 10,
    )

    highlight_fur_color = models.CharField(
            max_length = 10,
    )

    combination_of_primary_and = models.CharField(
            help_text = _('combination of previous two columns'),
            max_length = 30,
    )

    color_notes = models.CharField(
            max_length = 100,
    )

    location = models.CharField(
            max_length = 20,
    )

    above_ground_sighter = models.CharField(
            max_length = 10,
    )

    specific_location = models.CharField(
            max_length = 100,
    )

    running = models.BooleanField()

    chasing = models.BooleanField()

    climbing = models.BooleanField()

    eating = models.BooleanField()

    foraging = models.BooleanField()

    other_activities = models.CharField(
            max_length = 50,
    )

    kuks = models.BooleanField()

    quaas = models.BooleanField()

    moans = models.BooleanField()
    
    tail_flags = models.BooleanField()

    tail_twitches = models.BooleanField()

    approaches = models.BooleanField()

    indifferent = models.BooleanField()

    runs_from = models.BooleanField()

    other_interactions = models.CharField(
            max_length = 50,
    )

    lat_long = models.PointField()

    zip_codes = models.CharField(max_length=10)

    community_districts = models.IntegerField()

    borough_boundaries = models.IntegerField()

    city_council_districts = models.IntegerField()

    police_precincts = models.IntegerField()

    def __str__(self):
        return self.Unique_Squirrel_ID
