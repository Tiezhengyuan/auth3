from django.db import models

# Create your models here.


class Owner(models.Model):
    name = models.CharField(max_length=10)

    class Meta:
        app_label = 'reporting'


class Session(models.Model):
    name = models.CharField(max_length=10)

    class Meta:
        app_label = 'reporting'