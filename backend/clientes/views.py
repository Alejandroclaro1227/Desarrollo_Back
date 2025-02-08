from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from .models import Cliente, Compra
import pandas as pd
from datetime import datetime, timedelta
from django.db.models import Sum

# Create your views here.

def buscar_cliente(request):
    numero_documento = request.GET.get('numero_documento')
    try:
        cliente = Cliente.objects.get(numero_documento=numero_documento)
        compras = cliente.compras.select_related('producto').all()
        compras_data = [{
            'producto': compra.producto.nombre,
            'cantidad': compra.cantidad,
            'monto': compra.monto,
            'fecha': compra.fecha
        } for compra in compras]
        
        data = {
            'numero_documento': cliente.numero_documento,
            'nombre': cliente.nombre,
            'apellido': cliente.apellido,
            'correo': cliente.correo,
            'telefono': cliente.telefono,
            'tipo_documento': cliente.tipo_documento.nombre,
            'compras': compras_data
        }
        return JsonResponse(data)
    except Cliente.DoesNotExist:
        return JsonResponse({'error': 'Cliente no encontrado'}, status=404)

def exportar_cliente(request):
    numero_documento = request.GET.get('numero_documento')
    try:
        cliente = Cliente.objects.get(numero_documento=numero_documento)
        data = {
            'Número de Documento': cliente.numero_documento,
            'Nombre': cliente.nombre,
            'Apellido': cliente.apellido,
            'Correo': cliente.correo,
            'Teléfono': cliente.telefono,
        }
        df = pd.DataFrame([data])
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = f'attachment; filename=cliente_{numero_documento}.csv'
        df.to_csv(response, index=False)
        return response
    except Cliente.DoesNotExist:
        return JsonResponse({'error': 'Cliente no encontrado'}, status=404)

def exportar_clientes_fidelizados(request):
    # Obtener la fecha de hace un mes
    hace_un_mes = datetime.now() - timedelta(days=30)
    
    # Filtrar clientes con compras en el último mes
    clientes = Cliente.objects.annotate(
        total_compras=Sum('compras__monto', filter=Compra.objects.filter(fecha__gte=hace_un_mes))
    ).filter(total_compras__gt=5000000)
    
    # Preparar los datos para el reporte
    data = [{
        'Número de Documento': cliente.numero_documento,
        'Nombre': cliente.nombre,
        'Apellido': cliente.apellido,
        'Correo': cliente.correo,
        'Teléfono': cliente.telefono,
        'Total Compras': cliente.total_compras
    } for cliente in clientes]
    
    # Crear un DataFrame de Pandas
    df = pd.DataFrame(data)
    
    # Generar el archivo Excel
    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename=clientes_fidelizados.xlsx'
    df.to_excel(response, index=False)
    
    return response

def index(request):
    return render(request, 'index.html')

def lista_compras(request):
    compras = Compra.objects.select_related('cliente', 'producto').all()
    return render(request, 'compras.html', {'compras': compras})

def detalle_cliente(request, numero_documento):
    try:
        cliente = Cliente.objects.get(numero_documento=numero_documento)
        compras = cliente.compras.select_related('producto').all()
        return render(request, 'detalle_cliente.html', {'cliente': cliente, 'compras': compras})
    except Cliente.DoesNotExist:
        return render(request, 'error.html', {'mensaje': 'Cliente no encontrado'})
