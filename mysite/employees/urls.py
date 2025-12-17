from django.urls import path
from . import views

urlpatterns = [
    path('<int:pk>/', views.employee_detail,name='employee_details'),#employee/1/, pk-primary key or we can use employee_id
]