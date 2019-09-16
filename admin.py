# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import AppDriver, AppUser, Ride

admin.site.register(AppUser)
admin.site.register(AppDriver)
admin.site.register(Ride)
