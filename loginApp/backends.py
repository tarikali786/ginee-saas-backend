from django.contrib.auth.backends import ModelBackend
from .models import CustomUsers,CustomUsersV2

class SSOAuthBackend(ModelBackend):
    def authenticate(self, email=None):
        try:
            user = CustomUsersV2.objects.get(email=email)
            return user
        except ObjectDoesNotExist:
            # Run the default password hasher once to reduce the timing
            # difference between an existing and a non-existing user (#20760).
            # CustomUsersV2().set_password(password)
            pass