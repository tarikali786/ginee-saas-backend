from rest_framework import serializers

from django.conf import settings

from .models import PersonaModel,Devices,DigitalApps,Technology,Motivation,Personality



class PersonaSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = PersonaModel
        fields = '__all__'


    

    # def create(self, validated_data):

    #     persona = PersonaModel(

    #         age               =   validated_data['age'],
    #         annual_income     =   validated_data['annual_income'],
    #         bio               =   validated_data['bio'],
    #         children_count    =   validated_data['children_count'],
            
            
    #         dob               =   validated_data['dob'],
    #         frustrations      =   validated_data['frustrations'],
    #         gender            =   validated_data['gender'],
    #         location          =   validated_data['location'],
    #         marital_status    =   validated_data['marital_status'],
            
    #         name              =   validated_data['name'],
    #         needs             =   validated_data['needs'],
    #         occupation        =   validated_data['occupation'],
    #         persona_name      =   validated_data['persona_name'],
            
    #         profile_image     =   validated_data['profile_image'],
    #         quote             =   validated_data['quote'],
            
    #         values            =   validated_data['values']
    #     )

    #     devices           =   validated_data['devices']
    #     digital_apps      =   validated_data['digital_apps']
    #     technology        =   validated_data['technology']

    #     motivations       =   validated_data['motivations'],
    #     personality       =   validated_data['personality'],


    #     persona.save()


    #     for device in devices:
    #         persona.devices.add(Devices.objects.get(device=settings.PERSONA_DEVICES[device]))

    #     for dig in digital_apps:
    #         persona.digital_apps.add(DigitalApps.objects.get(digital=settings.PERSONA_DEVICES[dig]))

    #     for tech in technology:
    #         persona.technology.add(Technology.objects.get(technology=settings.PERSONA_DEVICES[tech]))
        

    #     persona.motivations.add(Motivation.objects.get(id=2))

    #     persona.personality.add(Personality.objects.get(id=1))


        # for device in devices:
        #     persona.devices.add(Devices.objects.get(id=2))

        # for dig in digital_apps:
        #     persona.digital_apps.add(DigitalApps.objects.get(id=2))

        # for tech in technology:
        #     persona.technology.add(Technology.objects.get(id=2))

        # persona.save()

        # return persona

