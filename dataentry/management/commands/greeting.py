from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'Greet the user'
    
    def add_arguments(self, parser):
        parser.add_argument('name', type=str, help='Specifies the user name')
    
    def handle(self, *args, **kwargs):
        name = kwargs['name']
        greet = f'Hi {name}, Wellcome'
        return self.stdout.write(greet)