# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class AppUser(models.Model):
    user = models.OneToOneField(User)
    phone_no = models.IntegerField()
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.user.username


class AppDriver(models.Model):
    user = models.OneToOneField(User)
    phone = models.IntegerField()
    loc = models.CharField(max_length=100)

    def __str__(self):
        return self.user.username


class Ride(models.Model):
    rider = models.OneToOneField(AppUser)
    driver = models.OneToOneField(AppDriver, null=True, blank=True)
    is_current_ride = models.BooleanField(default=True)
    status = models.CharField(max_length=15, default="Pending")

