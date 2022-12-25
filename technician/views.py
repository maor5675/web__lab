from django.shortcuts import redirect, render
from instruments.models import Malfunction
from django.contrib import messages

 

     
def change(request,data): 
    data = data.split(",")
    Customers = Malfunction.objects.filter( user_id = data[0], id = data[1] ).update(status = '3' )
    messages.success(request, 'Nice work,The order was transferred to another department ')
    return redirect('technician:mainpage') 
    