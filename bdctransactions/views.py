from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .forms import BdcclientForm, BdctranzactionForm

# Create your views here.

@login_required
def addclient(request):
    if request.method == "POST":
        client = BdcclientForm(request.POST)
        if client.is_valid():
           hsd = client.save(commit=False)
           hsd.bdc_id = request.user.bdcstaff.bdc_id
           hsd.added_by_id = request.user.id
           hsd.save()
           return render(request,'addclient.html', {'form': BdcclientForm, 'cmessage': "Client Added"})

    else:
        client = BdcclientForm

    return render(request, 'addclient.html', {'form': BdcclientForm})

@login_required
def addtransaction(request):
    if request.method == "POST":
        tranzact = BdctranzactionForm(data=request.POST)
        if tranzact.is_valid():
            trz = tranzact.save(commit=False)
            trz.bdc_id = request.user.bdcstaff.bdc_id
            trz.trans_by_id = request.user.id
            trz.save()
            return render(request, 'addtransaction.html', {'form': BdctranzactionForm, 'tmessage': "tranzaction Added Successfully"})

    else:
        tranzact = BdctranzactionForm

    return render(request, 'addtransaction.html', {'form': BdctranzactionForm})


