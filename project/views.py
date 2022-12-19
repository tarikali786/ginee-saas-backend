import requests
import json

from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication,BasicAuthentication
from django.contrib.sessions.models import Session

from loginApp.models import CustomUsers

from django.middleware.csrf import get_token
from django.http import JsonResponse


def csrf(request):
    return JsonResponse({'csrfToken': get_token(request)})
