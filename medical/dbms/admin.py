from django.contrib import admin
from .models import *

admin.site.register(Customer)
admin.site.register(Medicine)
admin.site.register(Agent)
admin.site.register(Employee)
admin.site.register(Invoice)