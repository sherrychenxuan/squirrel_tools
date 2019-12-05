from django.core.management.base import BaseCommand
from findsquirrels.models import Squirrel

class Command(BaseCommand):
    help = 'import squirrel.csv'

    def add_arguments(self,parser):
        parser.add_argument('csv_file', type = str)
    def handle(self,*args,**options):
        with open(options['csv_file'] as fp:
            reader = csv.DictReader(fp)
            data = list(reader)
        for item in data:
            p = Squirrel(



            )
            p.save()

