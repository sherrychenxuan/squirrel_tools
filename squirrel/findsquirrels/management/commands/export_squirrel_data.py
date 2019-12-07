from django.core.management.base import BaseCommand
from findsquirrels.models import Squirrel
import csv

class Command(BaseCommand):
    help = 'export squirrel.csv'
    def add_arguments(self,parser):
        parser.add_argument('csv_file', type = str)
    def handle(self,*args,**options):
        fp = open(options['csv_file'],'w')
        fields = [f.name for f in Squirrel._meta.get_fields()]
        writer = csv.writer(fp,fields)
        all_squirrel = Squirrel.objects.all()
       # field_names = [field.name for field in self.model._meta.fields]
        writer.writerow(fields)
        for item in all_squirrel:
            writer.writerow([getattr(item,str(f)) for f in fields])
