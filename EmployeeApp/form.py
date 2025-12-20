from django.forms import ModelForm
from .models import *

class AddEmployee(ModelForm):
    class Meta():
        model=EmployeeApp
        fields="__all__"

