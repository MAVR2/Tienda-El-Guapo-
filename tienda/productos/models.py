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
            ('es_admin', 'Puede gestionar productos'),
            ('es_comprador', 'Puede comprar productos'),
        ]
    
class Compra(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    
    def __str__(self):
        return f"{self.producto.precio} -- {self.producto.nombre}"
    
    class Meta:
        permissions = [
            ('es_admin', 'Puede ver ventas'),
            ('es_comprador', 'Puede ver solo sus compras'),
    ]