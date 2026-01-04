from django.shortcuts import render,redirect
from .models import*
from .form import*
from django.contrib.auth.decorators import login_required


# Create your views here.

@login_required(login_url="/")
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

@login_required(login_url="/")
def display(request):
    context={"emp":EmployeeApp.objects.all()}
    return render(request,"display.html",context)

@login_required(login_url="/")
def update_page(request,emp_1):
    emp=EmployeeApp.objects.get(id=emp_1)
    context={"addemp":AddEmployee(instance=emp)}
    if request.method == "POST":
      emp2=AddEmployee(request.POST,instance=emp)
      if emp2.is_valid():
         emp2.save()
         return redirect("/display/")
    return render(request,"form.html",context)

@login_required(login_url="/")
def delete_page(request,emp_2):
    emp=EmployeeApp.objects.get(id=emp_2)
    emp.delete()
    return redirect("/display/")

   



