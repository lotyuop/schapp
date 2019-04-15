from django import forms
from accounts.models import BdcProfile, BdcStaff
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ('username','password','email','first_name','last_name')

class BdcProfileForm(forms.ModelForm):
     class Meta:
         model = BdcProfile
         fields = ('bdc_name','bdc_short_name','contactp','phone','address','bdc_logo')

class BdcStaffForm(forms.ModelForm) :
    class Meta:
        model = BdcStaff
        fields = ['boss']