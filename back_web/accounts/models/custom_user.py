from django.contrib.auth.models import AbstractUser, \
    UserManager, PermissionsMixin
from django.db import models
from django.utils import timezone

from .custom_group import CustomGroup


class CustomUserManager(UserManager):
    pass


class CustomUser(AbstractUser, PermissionsMixin):
    custom_group = models.ManyToManyField(
        CustomGroup,
        blank = True,
        related_name='user_group',
        related_query_name='user',
    )
    
    objects = CustomUserManager()

    class Meta:
        app_label = 'accounts' 
    
    def __str__(self):
        return self.username