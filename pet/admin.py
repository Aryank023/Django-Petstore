from django.contrib import admin
from .models import pet
# Register your models here.
class petadmin(admin.ModelAdmin):
    prepopulated_fields={'slug':('name','species','breed')}
admin.site.register(pet,petadmin)
