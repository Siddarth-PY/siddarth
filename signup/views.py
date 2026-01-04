from django.shortcuts import render,redirect
from .models import*
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Create your views here.
def login_page(request):
    context={
        "error":"invalid"
    }
    if  request.method == "POST":
        emp=authenticate(username=request.POST["User"],
        password=request.POST["PASSWORD"]     )         
        
        if emp is not None:
          login(request,emp)
          if emp.username == "siddu":
           return redirect("/form/")
          else:
             return redirect("/display/")
        else:
            context={"error":"Invalid content"}
            return render(request,"login.html",context)
    return render(request,"login.html",context)


def signup_page(request):
 context={"error":"Invalid content"}
 if request.method =="POST":
    emp=User(username=request.POST["User"],
         first_name=request.POST["FIRSTNAME"],
         last_name=request.POST["LASTNAME"],
         email=request.POST["EMAIL"],
         DOB=request.POST["DOB"],
         Mobile=request.POST["MOBILE"],
         )
    emp.set_password(request.POST["PASSWORD"])
    emp.save()
 else:
    pass
 return render(request,"signup.html",context)


def logout_page(request):
   logout(request)
   return redirect("/")