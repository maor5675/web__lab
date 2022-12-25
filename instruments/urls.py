from django.urls import path
from . import views,user_func

app_name = 'lab'

urlpatterns = [
   path('search/', views.search, name="search"),
   path('login/', user_func.elogin, name="login"),
   path('logout/', user_func.elogout, name="logout"),
   path('register/', user_func.eregister, name="register"),
   path('lab/', views.brand, name="brand"),
   path('lab/<br>/', views.type, name="type"),
   path('lab/<br>/hitch', views.useraction, name="data"),
   path('lab/<br>/<mu>/<ui>', views.add_data, name="add_data"),



]