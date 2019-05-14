from django.db import models

# Create your models here.
class Employee(models.Model):
    ename=models.CharField(max_length=30)
    eid=models.IntegerField()
    esalary=models.IntegerField()
    eadd=models.CharField(max_length=30)
