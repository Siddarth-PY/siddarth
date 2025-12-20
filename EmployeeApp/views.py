from django.shortcuts import render,redirect
from .models import*
from .form import*

# Create your views here.
def formpage(request):
    context={"addemp":AddEmployee()}
    if request.method == "POST":
       print(request.POST)
       emp=AddEmployee(request.POST)
       if emp.is_valid():
          
           emp.save()
       else:
                      print("❌ Form errors:") 

    return render(request,"form.html",context)

def display(request):
    context={"emp":EmployeeApp.objects.all()}

    return render(request,"display.html",context)

def update_page(request,emp_1):
    emp=EmployeeApp.objects.get(id=emp_1)
    context={"addemp":AddEmployee(instance=emp)}
    if request.method == "POST":
      emp2=AddEmployee(request.POST,instance=emp)
      if emp2.is_valid():
         emp2.save()
         return redirect("/display/")
    return render(request,"form.html",context)


def delete_page(request,emp_2):
    emp=EmployeeApp.objects.get(id=emp_2)
    emp.delete()
    return redirect("/display/")

   



