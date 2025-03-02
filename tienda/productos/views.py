from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Producto, Compra

from .forms import ProductoForm, CompraForm

def lista_productosInicio(request):
    productos = Producto.objects.all()
    return render(request, 'productos/lista.html', {'productos': productos})

@login_required
def lista_productos(request):
    productos = Producto.objects.all()
    return render(request, 'productos/lista_productos.html', {'productos': productos})

@login_required
def crear_producto(request):
    if request.method == 'POST':
        if request.method == 'POST':
            form = ProductoForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                return redirect('lista_productos')
    else: form = ProductoForm()
    return render(request, 'productos/crear_producto.html'), {'form': form}

@login_required
def editar_producto(request, producto_id):
    producto = Producto.objects.get(id=producto_id)
    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('lista_productos')
    else:
        form = ProductoForm(instance=producto)
    return render(request, 'productos/editar_producto.html', {'form': form})

@login_required
def lista_ventas(request):
    ventas = Compra.objects.all()
    return render(request, 'productos/lista_ventas.html', {'ventas': ventas})

@login_required
def historial_compras(request):
    compras = Compra.objects.filter(usuario=request.user)
    return render(request, 'productos/historial_compras.html', {'compras': compras})


@login_required
def comprar(request, producto_id):
    producto = Producto.objects.get(id=producto_id)
    if request.method == 'POST':
        form = CompraForm(request.POST)
        if form.is_valid():
            compra = form.save(commit=False)
            compra.usuario = request.user
            compra.producto = producto
            compra.save()
            return redirect('historico_compras')
    else:
        form = CompraForm()
    return render(request, 'productos/comprar.html', {'form': form, 'producto': producto})
    


