from rest_framework.authentication import TokenAuthentication, get_authorization_header
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.authtoken.models import Token
import pytz
import datetime


class ExpiringTokenAuthentication(TokenAuthentication):
    def authenticate_credentials(self, key):

        try:
            token = Token.objects.get(key=key)

        except Token.DoesNotExist:
            raise AuthenticationFailed('Invalid Token')

        utc_now = datetime.datetime.utcnow()
        utc_now = utc_now.replace(tzinfo=pytz.utc)


        if token.created < utc_now - datetime.timedelta(seconds=3600):
            raise AuthenticationFailed('Token has Expired')

        return token.user, token