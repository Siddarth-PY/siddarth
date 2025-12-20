from django.db import models

# Create your models here.
class EmployeeApp(models.Model):
    emp_name=models.CharField(max_length=50)
    department=models.CharField(max_length=50)
    salary=models.BigIntegerField(default=0)
    doj=models.DateField()
    mobile_number=models.BigIntegerField(default=0)
    city=models.CharField(max_length=50)

def __str__(self):
    return self.empname

