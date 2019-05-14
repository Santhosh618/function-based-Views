import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','fbvproject.settings')
import django
django.setup()

from faker import Faker
from fbvApp.models import Employee
from random import *


fake=Faker()
def fakedata(n):
    for i in range(n):
        fname=fake.name()
        fid=fake.random_number(10,99)
        fsalary=fake.random_number(3)
        fadd=fake.address()
        fake_list=Employee.objects.get_or_create(ename=fname,eid=fid,esalary=fsalary,eadd=fadd)
fakedata(10)
