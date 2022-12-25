from django import forms
from django.shortcuts import redirect, render
from instruments.models import Malfunction

#that function target to send to the User personal Details menu
def mainprofile(request):
    return render(request, 'menu.html')

# send to the table the specific User personal Details
def orderstatus(request,ud):
    data = Malfunction.objects.filter(user_id = ud )
    context ={
    'customers': data,
    'action' : 'user'        
    }
    return render (request,'firsttable.html',context )


def done(request,data):
    data = data.split(",")
    Customers = Malfunction.objects.filter( user_id = data[0], id = data[1] ).update(status = '5' )
    return redirect('profile:orderstatus', ud = data[0]) 
    