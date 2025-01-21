from django.contrib import admin
from django.urls import path, include
from inicio.views import index

urlpatterns = [
    path('', index),
    path('admin/', admin.site.urls),
    path('produtos/', include('produtos.urls')),
    path('clientes/', include('clientes.urls')),
]