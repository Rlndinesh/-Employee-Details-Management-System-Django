from django.shortcuts import render
from django.http import Http404, HttpResponse
from django.shortcuts import get_object_or_404
from employees.models import Employee

# Create your views here.
def employee_detail(request, pk):

    employee=get_object_or_404(Employee, pk=pk)
    # return HttpResponse(f"<h2>Employee Name: {employee.first_name} {employee.last_name}</h2><br><h3>Designation: {employee.designation}</h3><br><h3>Email: {employee.email_address}</h3><br><h3>Phone Number: {employee.phone_number}</h3><br><img src='{employee.photo.url}' alt='No Image' width='200' height='200'>")
    # return render(request,'employee_detail.html')
    context={
        'employee':employee
    }
    return render(request,'employee_detail.html',context)
    # try:
    #     employee=Employee.objects.get(pk=pk)
    # except :
    #     raise Http404
