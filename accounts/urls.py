from django.conf.urls import url
from . import views

# SET THE NAMESPACE!
app_name = 'accounts'

# Be careful setting the name to just /login use userlogin instead!
urlpatterns=[
    url(r'^register/$',views.register,name='register'),
    url(r'^user_login/$',views.user_login,name='user_login'),

    url(r'^addstaff/$',views.add_staff,name='add_staff'),
    url(r'^home/$',views.home,name='home'),
]