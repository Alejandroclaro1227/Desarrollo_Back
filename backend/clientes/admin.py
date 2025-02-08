from django.contrib import admin
from .models import TipoDocumento, Cliente, Compra, Producto

# Register your models here.
admin.site.register(TipoDocumento)
admin.site.register(Cliente)
admin.site.register(Compra)
admin.site.register(Producto)
