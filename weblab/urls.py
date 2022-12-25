from django.contrib import admin
from django.urls import include, path
from instruments import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('lab/', include('instruments.urls')),
    path('userprofile/', include('user.urls')),
    path('transport/', include('transport.urls')),
    path('technician/', include('technician.urls')),
    path('',views.mainlab )
]

#http://127.0.0.1:8000/lab