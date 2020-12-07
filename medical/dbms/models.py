from django.db import models


class Customer(models.Model):
    customer_name = models.CharField(max_length=50, null=True)
    phone = models.CharField(max_length=12, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    total_amount = models.IntegerField()

    def __str__(self):
        return self.customer_name


class Medicine(models.Model):
    desc = (
        ('yes', 'yes'),
        ('no', 'no')
    )
    ware = (
        ('store', 'store'),
        ('upstairs', 'upstairs'),
        ('warehouse', 'warehouse')
    )
    med_name = models.CharField(max_length=50, null=True)
    manufacture_date = models.DateTimeField()
    expiry_date = models.DateTimeField()
    description = models.CharField(max_length=5, choices=desc)
    warehouse = models.CharField(max_length=10, choices=ware)

    def __str__(self):
        return self.med_name


class Agent(models.Model):
    agent_name = models.CharField(max_length=50, null=True)
    stock = models.IntegerField()
    total_amount = models.FloatField()
    med_id = models.ForeignKey(Medicine, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.agent_name


class Employee(models.Model):
    loc = (
        ('store', 'store'),
        ('upstairs', 'upstairs'),
        ('warehouse', 'warehouse')
    )
    emp_name = models.CharField(max_length=50, null=True)
    emp_phone = models.CharField(max_length=12, null=True)
    location = models.CharField(max_length=10, choices=loc)
    emp_salary = models.IntegerField()

    def __str__(self):
        return self.emp_name


class Invoice(models.Model):
    customer_id = models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL)
    employee_id = models.ForeignKey(Employee, null=True, on_delete=models.SET_NULL)
    medicine_id = models.ForeignKey(Medicine, null=True, on_delete=models.SET_NULL)
    bill_date = models.DateTimeField(auto_now_add=True)


