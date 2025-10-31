from django.core.management.base import BaseCommand, CommandError
import csv 
from dataentry.models import Student
from django.apps import apps
import datetime

'''
class Command(BaseCommand):
    help = 'Exporting data from Student Model to a csv file'
    
    def handle(self, *args, **kwargs):
        students = Student.objects.all()
        
        timestamp = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        file_path = f"exported_students_data_{timestamp}.csv"
        
        with open(file_path, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Roll No', 'Name', 'Age'])
            
            for student in students:
                writer.writerow([student.roll_no,student.name,student.age])
                
        return self.stdout.write(self.style.SUCCESS('Data exported successfully'))
'''

# proposed command = py manage.py exportdata model_name

class Command(BaseCommand):
    help = 'exporting data from database to a csv file'
    
    def add_arguments(self, parser):
        parser.add_argument('model_name', type=str, help="model name")
        
    def handle(self, *args, **kwargs):
        model_name = kwargs['model_name'].capitalize()
        
        model = None
        for app_config in apps.get_app_configs():
            try:
                model = apps.get_model(app_config.label, model_name)
                break
            except LookupError:
                pass
            
        if not model:
            self.stderr.write(f'model "{model_name}" cound not found in any app.')
            return
        
        data =model.objects.all()
        timestamp = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        file_path = f"exported_{model_name}_data_{timestamp}.csv"
        
        with open(file_path, 'w', newline='') as file:
            writer = csv.writer(file)
            
            # we want to print the field names of the model that we are trying to export
            writer.writerow([field.name for field in model._meta.fields])
            
            for row in data:
                writer.writerow([getattr(row, field.name) for field in model._meta.fields])
                
        self.stdout.write(self.style.SUCCESS('Data exported successfully'))