from __future__ import unicode_literals

from django.db import models
from .constatns import *

# Create your models here.


class User(models.Model):
    """User Model"""
    GENDER_CHOICES = ((MALE, 'Male'), (FEMALE, 'Female'))
    IS_ACTIVE_CHOICES = ((YES, 'Yes'), (NO, 'No'))
    TYPE_OF_USER_CHOICES = ((RETAILER, 'Retialer'), (CONSUMER, 'Consumer'))

    username = models.CharField(null=False, max_length=20, unique=True)
    password = models.CharField(null=False, max_length=20)
    gender = models.CharField(null=False, max_length=1,
                              choices=GENDER_CHOICES, default=MALE)
    type_of_user = models.CharField(
        null=False, max_length=1, choices=TYPE_OF_USER_CHOICES, default=RETAILER)
    is_active = models.CharField(
        null=False, max_length=1, choices=IS_ACTIVE_CHOICES, default=YES)
