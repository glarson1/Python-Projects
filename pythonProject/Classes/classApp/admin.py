from django.contrib import admin

# Register your models here.
from .models import djangoClasses

admin.site.register(djangoClasses) #registering the class that we imported from models