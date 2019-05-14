from django.contrib import admin
from fbvApp.models import Employee

# Register your models here.
class EmployeeAdmin(admin.ModelAdmin):
    list_display=['id','ename','eid','esalary','eadd']

admin.site.register(Employee,EmployeeAdmin)
