from django.shortcuts import render,redirect
from emp.models import Employee
from emp.forms import EmployeeForm

# Create your views here.
def entry(request):
    if request.method=="POST":
        form=EmployeeForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect("/show")
            except:
                pass
    else:
        form = EmployeeForm()
    return render(request,"index.html",{"form":form})

def show(request):
    employees=Employee.objects.all()
    return render(request,"show.html",{"employees":employees})

def edit(request,id):
    employees =Employee.objects.get(id=id)
    return render(request,"edit.html",{"employee":employees})


def update(request,id):
    employees = Employee.objects.get(id=id)
    form=EmployeeForm(request.POST,instance=employees)
    if form.is_valid():
        form.save()
        return redirect("/show")

    return render(request,"edit.html",{"employee":employees})


def delete(request,id):
    employee = Employee.objects.get(id=id)
    employee.delete()
    return redirect("/show")




