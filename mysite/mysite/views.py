from django.http import HttpResponse
from django.shortcuts import render
from employees.models import Employee

# def home(request):
#     return HttpResponse("<h3>Hello world</h3>")
def home(request):
    employees=Employee.objects.all()
    # print(employees)
    context={'employees':employees}
    return render(request,'home.html',context) 