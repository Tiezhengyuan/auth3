from django.contrib.auth.models import Group
from django.db import models

class CustomGroupManager(models.Manager):
    pass


class CustomGroup(Group):
    group_name = models.CharField(max_length=56)

    objects = CustomGroupManager()

    class Meta:
        app_label = 'accounts'
    
    def __str__(self):
        self.group_name

