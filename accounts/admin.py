from django.contrib import admin
from .models import BdcProfile, User, BdcStaff

# Register your models here.
admin.site.register(BdcProfile)
admin.site.register(BdcStaff)