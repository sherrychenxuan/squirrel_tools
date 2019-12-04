from django.db import models
from django.utils.translation import gettext as _

# Create your models here.
class Squirrel(models.Model):
    X = models.DecimalField(
            decimal_places = 18,
            max_digits = 22,
            help_text = _("Longitude coordinate for squirrel sighting point"),
    )

    Y = models.DecimalField(
            decimal_places = 18,
            max_digits = 22,
            help_text = _("Longitude coordinate for squirrel sighting point"),
    )

    Unique_Squirrel_ID = models.CharField(
            help_text = _('Identification tag for each squirrel sightings'),
            max_length = 30,
    )

    Hectare = models.CharField(
            help_text = _('Id tag'),
            max_length = 5,
    )

    Shift = models.CharField(
            help_text = _('sighting morning or afternoon'),
            max_length = 5,
    )

    Date = models.CharField(
            help_text = _('sighting day and month')
,
            max_length = 5,
    )

    Hectare_Squirrel_Number = models.IntegerField(
            help_text = _('number of squirrel sightings'),
    )

    def __str__(self):
        return self.Unique_Squirrel_ID
