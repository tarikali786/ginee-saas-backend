from django.contrib import admin
from .models import JsonModel
# Register your models here.

# class Designadmin(admin.ModelAdmin):
#     list_display=['user']
# @admin.register(JsonModel)
@admin.register(JsonModel)
class DegisnAdmin(admin.ModelAdmin):
    
    list_display=['user','jsondata']