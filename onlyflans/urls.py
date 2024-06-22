from django.contrib import admin
from django.urls import path, include
# onlyflans/web/urls.py
from web.views import index, about, welcome, contacto, exito

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('acerca/', about, name='about'),
    path('bienvenido/', welcome, name='welcome'),
    path('contacto/', contacto, name='contacto'),
    path('exito/', exito, name='exito'),
     path('accounts/', include('django.contrib.auth.urls')),

]

