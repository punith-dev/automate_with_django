from django.contrib import admin
from .models import Student, Customer, Employee

# Register your models here.

class studentAdmin(admin.ModelAdmin):
    list_display = ['roll_no', 'name', 'age']

class employeeAdmin(admin.ModelAdmin):
    list_display = ['employee_id', 'employee_name', 'designation', 'salary', 'retirement', 'other_benefits', 'total_benefits', 'total_compensation']


class customerAdmin(admin.ModelAdmin):
    list_display = ['customer_name', 'country']
    
admin.site.register(Student, studentAdmin)
admin.site.register(Customer, customerAdmin)
admin.site.register(Employee, employeeAdmin)