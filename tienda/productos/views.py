from django.views.generic import TemplateView, FormView
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.urls import reverse_lazy
from django.shortcuts import redirect, get_object_or_404
from .models import Producto, Compra
from .forms import ProductoForm, CompraForm, editarProductoForm


class ListaProductosInicioView(TemplateView):
    template_name = 'productos/lista.html'
    def get_context_data(self):
        lista = Producto.objects.all()
        return {    
            'productos': lista
            }

class ListaProductosView(PermissionRequiredMixin, TemplateView):
    template_name = 'productos/lista_productos.html'
    permission_required = 'productos.ver_producto'
    def get_context_data(self):
        lista = Producto.objects.all()
        return {    
            'productos': lista
            }
    def handle_no_permission(self):
        return redirect('login')

class CrearProductoView( FormView):
    template_name = 'productos/crear_producto.html'
    form_class = ProductoForm
    success_url = reverse_lazy('lista_productos')
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

class EditarProductoView(PermissionRequiredMixin, FormView):
    template_name = 'productos/editar_producto.html'
    permission_required = 'productos.cambiar_producto'
    form_class = editarProductoForm
    success_url = reverse_lazy('lista_productos')
    
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        id = self.kwargs.get('producto_id')
        producto = get_object_or_404(Producto, id=id)
        kwargs['instance'] = producto
        return kwargs
    
    def form_valid(self, form):
        form.save(self.kwargs.get('producto_id'))
        return super().form_valid(form)

class ListaVentasView(PermissionRequiredMixin, TemplateView):
    template_name = 'productos/lista_ventas.html'
    permission_required = 'productos.ver_compra'

    def get_context_data(self):
        lista = Compra.objects.all()
        return {    
            'compras': lista
            }

class HistorialComprasView(PermissionRequiredMixin, TemplateView):
    template_name = 'productos/historial_compras.html'
    permission_required = 'productos.ver_compra'

    def get_context_data(self):
        lista = Compra.objects.all()
        lista = Compra.objects.filter(usuario=self.request.user)
        return {
            'compras': lista
        }
        
class ComprarProductoView(PermissionRequiredMixin, FormView):
    template_name = 'productos/comprar.html'
    form_class = CompraForm
    permission_required = 'productos.agregar_compra'
    success_url = reverse_lazy('historico_compras')
    
    def get_context_data(self):
        context = super().get_context_data()
        producto = get_object_or_404(Producto, id=self.kwargs['producto_id'])
        context['producto'] = producto  
        return context

    def form_valid(self, form):
        producto = get_object_or_404(Producto, id=self.kwargs['producto_id'])
        form.save(
            producto=producto,
            usuario=self.request.user
        )
        return super().form_valid(form)



