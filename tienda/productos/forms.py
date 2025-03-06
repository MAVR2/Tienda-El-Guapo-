from django import forms
from .models import Producto, Compra

class editarProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'precio', 'imagen', 'estatus']
        labels = {
            'nombre': 'Nombre del producto',
            'precio': 'Precio del producto',
            'imagen': 'Imagen del producto',
            'estatus': 'Estatus del producto',
        }
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'precio': forms.NumberInput(attrs={'class': 'form-control'}),
            'imagen': forms.FileInput(attrs={'class': 'form-control'}),
            'estatus': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

    def save(self, id):
        producto = Producto.objects.filter(id=id).first()
        producto.nombre=self.cleaned_data['nombre']
        producto.precio=self.cleaned_data['precio']
        producto.imagen=self.cleaned_data['imagen']
        producto.estatus=True if self.cleaned_data['estatus'] else False
        
        producto.save()
        return producto

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'precio', 'imagen', 'estatus']
        labels = {
            'nombre': 'Nombre del producto',
            'precio': 'Precio del producto',
            'imagen': 'Imagen del producto',
            'estatus': 'Estatus del producto',
        }
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'precio': forms.NumberInput(attrs={'class': 'form-control'}),
            'imagen': forms.FileInput(attrs={'class': 'form-control'}),
            'estatus': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

    def save(self):
        producto = Producto(
            nombre=self.cleaned_data['nombre'],
            precio=self.cleaned_data['precio'],
            imagen=self.cleaned_data['imagen'],
            estatus=True if self.cleaned_data['estatus'] else False,
        )
        producto.save()
        return producto

class CompraForm(forms.ModelForm):
    class Meta:
        model = Compra
        fields = ['cantidad']
        
    def save(self, producto, usuario):
        compra = Compra(
            producto=producto,
            usuario=usuario,
            cantidad=self.cleaned_data['cantidad']
        )
        
        compra.save()
        return compra
