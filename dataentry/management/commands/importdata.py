from django.core.management.base import BaseCommand, CommandError
# from dataentry.models import Student
from django.apps import apps
import csv

'''
# Proposed command = py manage.py importdata file_path
class Command(BaseCommand):
    help = "Importing data from CSV file"
    
    def add_arguments(self, parser):
        parser.add_argument('file_path', type=str, help='Path to the csv file')
        
    def handle(self, *args, **kwargs):
        file_path = kwargs['file_path']
        print(file_path)
        with open(file_path, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                roll_no = row['roll_no']
                existsing_data = Student.objects.filter(roll_no=roll_no).exists()
                if not existsing_data:
                    Student.objects.create(**row)
                else:
                    self.stdout.write(self.style.WARNING(f'Student with {roll_no} is already exists!'))
        return self.stdout.write(self.style.SUCCESS('Data imported from CSV successfully'))
'''
    
# Proposed command = py manage.py importdata file_path model_name
class Command(BaseCommand):
    help = "Importing data from CSV file"
    
    def add_arguments(self, parser):
        parser.add_argument('file_path', type=str, help='Path to the csv file')
        parser.add_argument('model_name', type=str, help='Name of the model')
        
    def handle(self, *args, **kwargs):
        file_path = kwargs['file_path']
        model_name = kwargs['model_name'].capitalize()
        print(file_path)
        print(model_name)
        
        # Search for the Model across all installed apps
        model = None
        for app_config in apps.get_app_configs():
            try:
                model = apps.get_model(app_config.label, model_name)
                break
            except LookupError:
                continue
        if not model:
            raise CommandError(f'model "{model_name}" not found in any app.')
        
        
        with open(file_path, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                model.objects.create(**row)
        return self.stdout.write(self.style.SUCCESS('Data imported from CSV successfully'))