from urllib import request
from django.http import HttpResponse
from django.shortcuts import redirect, render
from instruments.models import Malfunction, Phonebrand, Phonetype,Phone,Malfunction_type
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def mainlab(request):
    context = {
        'brandlist': 'none'
    }        
    return render(request, 'brand.html', context)




# here i show to the costumers all the brands i have to ofer
def brand(request):
    brandlist = Phonebrand.objects.all()
    context = {
        'brandlist': brandlist,
    }
    return render(request, 'brand.html', context)


# here i show to the costumers all the phone types i have to ofer
@login_required
def type(request,br):
    typelist = Phonetype.objects.filter(brand = br)
    device = Phone.objects.all()
    context = {
        'typelist': typelist,
        'phones':device,

    }
    return render(request, 'phonetype.html', context)

# give the costumer the option to choose the problem he have 
def useraction(request,br):
    hitch = Malfunction_type.objects.all()
    context = {
        'hitches' : hitch,
        'type' : br
    }
    return  render(request,'malfu.html',context)


def search(request):
    send =  request.GET.get('search')
    result = Phone.objects.filter(device__contains = send) 
    context = {
        'results':result,
        'name':'search'
    }
    return render(request,'phonetype.html', context)


# insert the data to Malfunction table 
def add_data(request,br,mu,ui):
    userid = ui
    Status = 1
    malfunction = Malfunction(phone_id = br,Malfunction_type_id = mu, user_id = userid, status = Status)
    malfunction.save()
    messages.success(request, 'your request accepted')
    return redirect('/') 
