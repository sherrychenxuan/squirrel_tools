from django.core.management.base import BaseCommand
from findsquirrels.models import squirrel

class Command(BaseCommand):
    help = 'import squirrel.csv'

    def add_arguments(self,parser):
        parser.add_argument('path', type = str, help = 'The path of the csv file')
    def handle(self,*args,**kwargs):
        path = kwargs['path']
        print(path)

        p = squirrel(
                X = 123.1,
                Y = 456,
                Unique_Squirrel_ID = 'haha',
        )
        p.save()
        
        
