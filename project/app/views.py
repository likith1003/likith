from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from app.forms import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
# Create your views here.

def registration(request):
    EPFO = ProfileForm()
    EUFO = UserForm()
    d = {'EUFO':EUFO, 'EPFO':EPFO}
    if request.method == 'POST' and request.FILES:
        UFDO = UserForm(request.POST)
        PFDO = ProfileForm(request.POST, request.FILES)
        if UFDO.is_valid():
            MUFDO = UFDO.save(commit=False)
            pw = UFDO.cleaned_data.get('password')
            MUFDO.set_password(pw)
            MUFDO.save()
            MPFDO = PFDO.save(commit=False)
            MPFDO.username = MUFDO
            MPFDO.save()
            send_mail(
                "Registration",
                "Registration is Successfull",
                "likith.qsp@gmail.com",
                [MUFDO.email],
                fail_silently=False
            )
            return render(request, 'user_login.html')
        else:
            return HttpResponse('Invalid Data')
    return render(request, 'registration.html',d)

def user_login(request):
    if request.method == 'POST':
        un = request.POST.get('un')
        pw = request.POST.get('pw')
        AUO = authenticate(username=un, password=pw)
        if AUO and AUO.is_active:
            login(request, AUO)
            request.session['username']=un
            return HttpResponseRedirect(reverse('Homepage'))
    return render(request, 'user_login.html')

def index(request):
    if request.session.get('username'):
        un = request.session['username']
        uo = User.objects.get(username=un)
        d = {'uo':uo}
        return render(request, 'home.html', d)
    return render(request, 'home.html')

@login_required
def  user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('Homepage'))

@login_required
def user_profile(request):
    un = request.session.get('username')
    uo = User.objects.get(username=un)
    po = Profile.objects.get(username=uo)
    d = {'uo':uo, 'po':po}
    return render(request, 'user_profile.html', d)