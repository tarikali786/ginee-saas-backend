from rest_framework import serializers
from django.contrib.auth.models import User

from .models import CustomUsers,CustomUsersV2

from . import google, facebook
from .register import register_social_user
import os
from rest_framework.exceptions import AuthenticationFailed




class FacebookSocialAuthSerializer(serializers.Serializer):
    """Handles serialization of facebook related data"""
    auth_token = serializers.CharField()

    def validate_auth_token(self, auth_token):
        user_data = facebook.Facebook.validate(auth_token)
        
        try:
            user_id = user_data['id']
            email = user_data['email']
            name = user_data['name']
            provider = 'facebook'
            return register_social_user(
                provider=provider,
                user_id=user_id,
                email=email,
                name=name
            )
        except Exception as identifier:

            raise serializers.ValidationError(
                'The token  is invalid or expired. Please login again.'
            )


class GoogleSocialAuthSerializer(serializers.Serializer):
    auth_token = serializers.CharField()

    def validate_auth_token(self, auth_token):
        user_data = google.Google.validate(auth_token)
        try:
            user_data['sub']
        except:
            raise serializers.ValidationError(
                'The token is invalid or expired. Please login again.'
            )

        # if user_data['aud'] != os.environ.get('GOOGLE_CLIENT_ID'):

        #     raise AuthenticationFailed('oops, who are you?')
        print('user data is...',user_data)
        user_id = user_data['sub']
        email = user_data['email']
        first_name = user_data['name']
        last_name = user_data['family_name']
        name = [first_name,last_name]
        provider = 'google'

        request = self.context.get("request")
        return register_social_user(request,
            provider=provider, user_id=user_id, email=email, name=name)



class CustomRegistrationSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = CustomUsers
        fields = '__all__'

        extra_kwargs = {'password': {'write_only': True}}



    def create(self, validated_data):
        
        
        user = CustomUsers.objects.create_user(email=validated_data['email'],
                                                    first_name=validated_data['first_name'],
                                                    last_name=validated_data['last_name'],
                                                    phone=validated_data['phone'],
                                                    password=validated_data['password'])
        
        return user




class CustomRegistrationSerializerV2(serializers.ModelSerializer):
    
    class Meta:
        model = CustomUsersV2
        fields = '__all__'

        extra_kwargs = {'password': {'write_only': True}}


    def create(self, validated_data):
        
        
        user = CustomUsersV2.objects.create_user(email=validated_data['email'],
                                                    full_name=validated_data['full_name'],
                                                    organization = validated_data['organization'],                                               
                                                    password=validated_data['password'])
        
        return user






