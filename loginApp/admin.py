from django.contrib import admin

from .models import CustomUsers,CustomUsersV2


@admin.register(CustomUsers)
class CustomUsersAdmin(admin.ModelAdmin):
    
    readonly_fields=["password"]




@admin.register(CustomUsersV2)
class CustomUsersAdmin(admin.ModelAdmin):
    
    readonly_fields=["password"]