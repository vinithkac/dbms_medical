from django.shortcuts import render
from django.http import HttpResponse
from .models import *


def home(request):
    return render(request, 'dbms/index.html')


def home1(request):
    return render(request, 'dbms/index.html')


def agent(request, id=0):
    if id:
        agents = Agent.objects.filter(id=id)
    else:
        agents = Agent.objects.all()
        return render(request, 'dbms/agents.html', {'agents': agents})


def customer(request, id=0):
    if id:
        customers = Customer.objects.filter(id=id)
        return render(request, 'dbms/customers.html', {'customers': customers})
    else:
        customers = Customer.objects.all()
        return render(request, 'dbms/customers.html', {'customers': customers})


def invoice(request):
    invoices = Invoice.objects.all()
    return render(request, 'dbms/invoice.html', {'invoices': invoices})


def employee(request):
    emp = Employee.objects.all()
    return render(request, 'dbms/employee.html', {'emp': emp})


def medicine(request):
    med = Medicine.objects.all()
    return render(request, 'dbms/medical.html', {'med': med})


def join(request):
    joined = Agent.objects.select_related('med_id').all()
    print(joined.query)
    return render(request, 'dbms/join.html', {'joined': joined})


def about(request):
    return render(request, 'dbms/about.html')



