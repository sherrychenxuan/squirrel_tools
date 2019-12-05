from django.core.management.base import BaseCommand
from findsquirrels.models import Squirrel
import csv

class Command(BaseCommand):
    help = 'import squirrel.csv'

    def add_arguments(self,parser):
        parser.add_argument('csv_file', type = str)
    def handle(self,*args,**options):
        with open(options['csv_file']) as fp:
            reader = csv.DictReader(fp)
            data = list(reader)
        for item in data:
            p = Squirrel(
                x = item["X"],
                y = item["Y"],
                unique_squirrel_id = item["Unique Squirrel ID"],
                hectare = item["Hectare"],
                shift = item["Shift"],
                date = item["Date"],
                hectare_squirrel_number = item["Hectare Squirrel Number"],   
                age = item["Age"],
                primary_fur_color =item["Primary Fur Color"],
                highlight_fur_color = item["Highlight Fur Color"],
                combination_of_primary_and = item["Combination of Primary and Highlight Color"],
                color_notes = item["Color notes"],
                location = item["Location"],
                above_ground_sighter = item["Above Ground Sighter Measurement"],
                specific_location = item["Specific Location"],
                running = item["Running"],
                chasing = item["Chasing"],
                climbing = item["Climbing"],
                eating = item["Eating"],
                foraging = item["Foraging"],
                other_activities = item["Other Activities"],
                kuks = item["Kuks"],
                quaas = item["Quaas"],
                moans = item["Moans"],
                tail_flags = item["Tail flags"],
                tail_twitches = item["Tail twitches"],
                approaches = item["Approaches"],
                indifferent = item["Indifferent"],
                runs_from = item["Runs from"],
                other_interactions = item["Other Interactions"],
                lat_long = item["Lat/Long"],
                zip_codes = item["Zip Codes"],
                community_districts = item["Community Districts"],
                borough_boundaries = item["Borough Boundaries"],
                city_council_districts = item["City Council Districts"],
                police_precincts = item["Police Precincts"],
            )
            p.save()

