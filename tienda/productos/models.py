from django.db import models
from django.contrib.auth.models import User

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    imagen = models.ImageField(upload_to='productos/img/', null=True, blank=True)
    estatus = models.BooleanField(default=True)
    
    def __str__(self):
        return self.nombre

    class Meta:
        permissions = [
            ('ver_producto', 'Puede ver producto'),
            ('agregar_producto', 'Puede agregar producto'),
            ('cambiar_producto', 'Puede cambiar producto'),
        ]


class Compra(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    
    def __str__(self):
        return f"{self.producto.nombre} - {self.cantidad}"

    class Meta:
        permissions = [
            ('ver_compra', 'Puede ver compra'),
            ('agregar_compra', 'Puede agregar compra'), 
        ]