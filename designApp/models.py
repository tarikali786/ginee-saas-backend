from django.db import models
from loginApp.models import CustomUsersV2

class JsonModel(models.Model):
    jsondata = models.JSONField()
    user = models.ForeignKey(CustomUsersV2, related_name='user',null=True,blank=True, on_delete=models.CASCADE)
