from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class BdcProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bdc_name = models.CharField(max_length=150, verbose_name="BDC Name")
    bdc_short_name = models.CharField(max_length=20, unique=True, verbose_name="Short Name")
    phone = models.CharField(max_length=16,unique=True)
    address = models.TextField("Office Address")
    contactp = models.CharField(max_length=150, verbose_name="Contact Person")
    bdc_logo = models.ImageField(upload_to='profile_pics', blank=True)
    subscription_status = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username


class BdcStaff(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bdc = models.ForeignKey(BdcProfile, on_delete=models.CASCADE)
    boss = models.BooleanField(default=False)
    added_by = models.CharField(max_length=4, editable=False)
    added_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username
