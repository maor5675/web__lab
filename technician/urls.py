from django.urls import path
from . import views

app_name = 'technician'

urlpatterns = [
   path('<data>/', views.change, name="change"),

]   