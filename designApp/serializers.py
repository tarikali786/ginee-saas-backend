
from rest_framework import serializers
from .models import JsonModel



class JsonFileSerializer(serializers.ModelSerializer):
    # user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    # user = serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model = JsonModel
        fields = ('id','jsondata','user',)


   



