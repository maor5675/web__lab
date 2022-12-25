from django.urls import path
from . import views

app_name = 'transport'

urlpatterns = [
   path('', views.main_page_tran, name="mainpage"),
   path('mailman/', views.second_page_tran, name="mailman"),
   path('technician/', views.main_page_tech, name="technician"),
   path('<data>/', views.first_change, name="firstchange"),
   


]   