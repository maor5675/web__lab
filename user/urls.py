from django.urls import path
from . import views

app_name = 'profile'

urlpatterns = [
   path('', views.mainprofile, name="menu"),
 #  path('profile/', views.updateprofile, name="updateprofile"),
   path('<ud>', views.orderstatus, name="orderstatus"),
   path('done/<data>', views.done, name="lastaction"),
]
