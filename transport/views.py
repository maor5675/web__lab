from django.http import HttpResponse
from django.shortcuts import redirect, render
from instruments.models import Malfunction
from django.contrib import messages
from django.db.models import Q
 
# this function is for the first delivery afther the costumer make a order the mail man need to go to the place he insert to the web and take the phone 
def main_page_tran(request):
    Customers = Malfunction.objects.all()
    context = {
        'customers' :Customers,
        'action' : 'staff'

    }
    return  render(request,'firsttable.html',context)
     
def first_change(request,data):
    data = data.split(',')
    num =  int(data[2]) +1
    Customers = Malfunction.objects.filter( user_id = data[0], id = data[1]).update(status = num)
    messages.success(request, 'Nice work,The order was transferred to another department ')
    return redirect('/')    

#this function is for the second delivery the mail man take the phone from the technician and deliver the phone back to the cosumer
def second_page_tran(request):
    Customers = Malfunction.objects.filter(Q(status = '1') | Q(status ='3'))
    context = {
        'customers' :Customers,
        'action' : 'staff'
    }
    return  render(request,'firsttable.html',context)

def main_page_tech(request):
    Customers = Malfunction.objects.filter(status = '2')
    context = {
        'customers' :Customers,
        'action' : 'staff'

    }
    return  render(request,'firsttable.html',context)
