from  django.core.management.base import BaseCommand
from dataentry.models import Student

class Command(BaseCommand):
    help = "Insert data to the database"
    
    def handle(self, *args, **kwargs):
        dataset=[
            {"roll_no": 1002, "name":"Prabhu", "age":22},{"roll_no": 1003, "name":"sangu", "age":22},{"roll_no": 1004, "name":"abc", "age":21},{'roll_no': 1005, 'name': 'shashi','age':21}
        ]
        
        for data in dataset:
            roll_no = data['roll_no']
            existsing_data = Student.objects.filter(roll_no=roll_no).exists()
            
            if not existsing_data:
                Student.objects.create(roll_no = data['roll_no'], name = data['name'], age = data['age'])
                
            else :
                self.stdout.write(self.style.WARNING(f'Student with this {roll_no} already exists!'))
        return self.stdout.write(self.style.SUCCESS('Data inserted successfully'))