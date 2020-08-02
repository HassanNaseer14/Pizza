from django.contrib import admin
from .models import CreateMenuItem as c
from django.contrib.admin import site
# Register your models here.
admin.site.register(c)
