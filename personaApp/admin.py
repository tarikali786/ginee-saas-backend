from django.contrib import admin

from .models import Devices,PersonaModel,Technology,DigitalApps,Personality,Motivation


@admin.register(Devices)
class DevicesAdmin(admin.ModelAdmin):
    
    pass

@admin.register(Technology)
class TechnologyAdmin(admin.ModelAdmin):
    
    pass


@admin.register(DigitalApps)
class DigitalAppsAdmin(admin.ModelAdmin):
    
    pass

@admin.register(Personality)
class PersonalityAdmin(admin.ModelAdmin):
    
    pass



@admin.register(Motivation)
class MotivationAdmin(admin.ModelAdmin):
    
    pass



@admin.register(PersonaModel)
class PersonaModelAAdmin(admin.ModelAdmin):
    
    pass
