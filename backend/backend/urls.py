"""
URL configuration for backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from clientes.views import buscar_cliente, exportar_cliente, index, exportar_clientes_fidelizados, lista_compras, detalle_cliente

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/buscar_cliente/', buscar_cliente, name='buscar_cliente'),
    path('api/exportar_cliente/', exportar_cliente, name='exportar_cliente'),
    path('api/reporte-fidelizacion/', exportar_clientes_fidelizados, name='reporte_fidelizacion'),
    path('compras/', lista_compras, name='lista_compras'),
    path('cliente/<str:numero_documento>/', detalle_cliente, name='detalle_cliente'),
    path('', index, name='index'),
]
