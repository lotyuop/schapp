from django.conf.urls import url
from django.urls import path
from . import views

app_name = "bdctransactions"

urlpatterns=[
    path('addclient', views.addclient, name="addclient"),
    path('addtransaction', views.addtransaction, name="addtransaction")
]