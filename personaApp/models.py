from django.db import models
from django.conf import settings

from djongo.storage import GridFSStorage

grid_fs_storage = GridFSStorage(collection='persona_profile_images', base_url=''.join([settings.BASE_URL, '/profileimages/']))
# Create your models here.
class Devices(models.Model):

    device = models.CharField(max_length=10,blank=True,null=True)

    def __str__(self):
        return str(self.device)


class Technology(models.Model):

    technology = models.CharField(max_length=10,blank=True,null=True)

    def __str__(self):
        return str(self.technology)


class DigitalApps(models.Model):

    digital = models.CharField(max_length=10,blank=True,null=True)

    def __str__(self):
        return str(self.digital)


class Personality(models.Model):

    min_field = models.CharField(max_length=25,blank=True,null=True)
    max_field = models.CharField(max_length=25,blank=True,null=True)
    values    = models.IntegerField(null=True,blank=True)

    def __str__(self):
        return str(self.min_field)+'_'+str(self.max_field)


class Motivation(models.Model):

    motivation   = models.CharField(max_length=25,blank=True,null=True)
    percentage   = models.IntegerField(null=True,blank=True,default=0)

    def __str__(self):
        return str(self.motivation)


class PersonaModel(models.Model):

    persona_name    = models.CharField(max_length=255,blank=True,null=True)
    customer_name   = models.CharField(max_length=255,blank=True,null=True)
    profile_image   = models.ImageField(blank=True, null=True, upload_to='entries',storage=grid_fs_storage)
    gender          = models.CharField(max_length=10,blank=True,null=True)
    dob             = models.CharField(max_length=55,blank=True,null=True)
    age             = models.IntegerField()
    marital_status  = models.CharField(max_length=10,blank=True,null=True)
    children_count  = models.IntegerField(blank=True,null=True)
    location        = models.CharField(max_length=555,blank=True,null=True)
    occupation      = models.CharField(max_length=100,blank=True,null=True)
    annual_income   = models.IntegerField(blank=True,null=True)
    bio             = models.TextField(blank=True,null=True)
    quote           = models.TextField(blank=True,null=True)

    needs           = models.JSONField(null=True,blank=True)
    values          = models.JSONField(null=True,blank=True)
    frustrations    = models.JSONField(null=True,blank=True)
    

    devices         = models.ManyToManyField(Devices)
    technology      = models.ManyToManyField(Technology)
    digital_apps    = models.ManyToManyField(DigitalApps)
    personality     = models.ManyToManyField(Personality)
    motivations     = models.ManyToManyField(Motivation)


    def __str__(self):
        return str(self.customer_name)


