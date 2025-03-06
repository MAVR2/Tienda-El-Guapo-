from django.urls import path
from .views import (
    ListaProductosInicioView,
    ComprarProductoView,
    HistorialComprasView,
    ListaProductosView,
    CrearProductoView,
    EditarProductoView,
    ListaVentasView
)
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', ListaProductosInicioView.as_view(), name='lista_productos'),
    path('comprar/<int:producto_id>/', ComprarProductoView.as_view(), name='comprar'),
    path('historico/', HistorialComprasView.as_view(), name='historico_compras'),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('lista_productos/', ListaProductosView.as_view(), name='lista_productos'),
    path('crear_producto/', CrearProductoView.as_view(), name='crear_producto'),
    path('editar_producto/<int:producto_id>/', EditarProductoView.as_view(), name='editar_producto'),
    path('lista_ventas/', ListaVentasView.as_view(), name='lista_ventas'),
]
