from django import forms
from .models import BdcClient, Banks, BdcTranzactions, BdcTranzactions_Archive, Currency
from django.contrib.auth.models import User

class BdcclientForm(forms.ModelForm):
    class Meta:
        model = BdcClient
        fields = ['name', 'phone', 'email','bank','acct']

class BdctranzactionForm(forms.ModelForm):
    class Meta:
        model = BdcTranzactions
        fields = ['currency_sold', 'sold_amount', 'currency_bought', 'bought_amount', 'bank', 'client_acct', 'trans_date', 'comments']

class TransbaseForm(forms.Form):
    client=forms.CharField()