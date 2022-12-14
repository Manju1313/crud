from django.contrib import admin
from emp.models import *
from django.db import models

# Register your models here.
@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('eid','ename','eemail','econtact')
    list_filter = ['ename']
    list_per_page = 2 