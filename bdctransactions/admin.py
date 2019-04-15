from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Currency)
admin.site.register(BdcClient)
admin.site.register(BdcTranzactions)
admin.site.register(Banks)