from urllib import request

from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect


def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.info(request, 'username or password is incorrect')

        context = {}
        return render(request, 'main/login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('login')


def acceptPage(request):
    context = {}
    return render(request, 'main/accept.html', context)



'''''''''
def accept(request):
    submitted = False
    if request.method == "POST":
        form = AcceptForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/accept?submitted=True')
    else:
        form = AcceptForm
        if 'submitted' in request.GET:
            submitted = True

    return render(request, 'events/accept.html', {'form':form, 'submitted':submitted})
'''''


@login_required(login_url='login')
def homePage(request):
    context = {}
    return render(request, 'main/home.html', context)


@login_required(login_url='login')
def listOfMashinist(request, mash_id):
    mashids = Mash.objects.get(pk = mash_id)
    listOfMashinistt = Mash.objects.all()
    return render(request, 'main/list_of_mashinist.html', {
        'listOfMashinist': listOfMashinistt,
        'mashids': mashids
    })


@login_required(login_url='login')
def listOfCities(requst):
    listOfCitiess = Cities.objects.all()
    return render(request, 'main/list_of_mashinist.html', {
        'listOfCities': listOfCitiess
    })


@login_required(login_url='login')
def acceptMashinist(request, mash_id):
    mashids = Mash.objects.get(pk=mash_id)
    context = {'mashids': mashids}
    return render(request, 'main/accept.html', context)


@login_required(login_url='login')
def currentRoute(request):
    context = {}
    return render(request, 'main/current_route.html', context)

