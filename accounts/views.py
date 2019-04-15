from django.shortcuts import render
from .forms import UserForm, BdcProfileForm, BdcStaffForm

from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required

# Create your views here.



def index(request):
    return render(request,'index.html')

@login_required
def home(request):
    return render(request,'accounts/home.html')

@login_required
def special(request):
    return HttpResponse("You are logged in !")

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

def register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = BdcProfileForm(data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user

            if 'bdc_logo' in request.FILES:
                print('found it')
                profile.bdc_logo = request.FILES['bdc_logo']
            profile.save()
            registered = True
            bdcstaff = BdcStaffForm().save(commit=False)
           
            bdcstaff.user = user
            bdcstaff.bdc = profile
            bdcstaff.boss = True
            bdcstaff.save()
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = BdcProfileForm()
    return render(request,'accounts/registration.html',{'user_form':user_form,'profile_form':profile_form,'registered':registered})

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request,user)
               # request.session['userid']=user.id
                return HttpResponseRedirect(reverse('accounts:home'))
            else:
                return render(request, 'accounts/login.html', {'login_message': 'The user has been removed', })
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username,password))
           # return HttpResponse("Invalid login details given")
        return render(request, 'accounts/login.html', {'login_message': 'Invalid login details given', })
    else:
        return render(request, 'accounts/login.html', {})



@login_required
def add_staff(request) :
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        if user_form.is_valid():
            staff = user_form.save()
            staff.set_password(staff.password)
            staff.save()
            stafftab = BdcStaffForm().save(commit=False)
            stafftab.user = staff
            stafftab.bdc_id = request.user.bdcstaff.bdc_id
            stafftab.boss = False;
            stafftab.save()
            registered = True
        else:
            print(user_form.errors)
    else:
        user_form = UserForm()

    return render(request, 'accounts/addstaff.html',
                  {'user_form': user_form, 'registered': registered})

