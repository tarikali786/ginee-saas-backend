
from django.contrib.auth import authenticate,login
from .models import CustomUsers
import os
import random
from rest_framework.exceptions import AuthenticationFailed


def generate_username(name):

    username = "".join(name.split(' ')).lower()
    if not CustomUsers.objects.filter(username=username).exists():
        return username
    else:
        random_username = username + str(random.randint(0, 1000))
        return generate_username(random_username)


def register_social_user(request, provider, user_id, email, name):
    filtered_user_by_email = CustomUsers.objects.filter(email=email)

    if filtered_user_by_email:

        if provider == filtered_user_by_email[0].auth_provider:

            # registered_user = authenticate(
            #     email=email, password=os.environ.get('SOCIAL_SECRET'))

            registered_user = authenticate(
                email=email, password='12345')
            
            login(request, registered_user)

            return {
                # 'username': registered_user.username,
                'email': registered_user.email,
                'tokens': registered_user.tokens()}

        else:
            raise AuthenticationFailed(
                detail='Please continue your login using ' + filtered_user_by_email[0].auth_provider)

    else:
        user = {
            'first_name' : name[0],
            'last_name' : name[1],
             'email': email,
            # 'password': os.environ.get('SOCIAL_SECRET')
            'password': '12345'
            }
        user = CustomUsers.objects.create_user(**user)
        user.is_verified = True
        user.auth_provider = provider
        user.save()

        new_user = authenticate(
            email=email, password='12345')
        return {
            'email': new_user.email,
            # 'username': new_user.username,
            'tokens': new_user.tokens()
        }
