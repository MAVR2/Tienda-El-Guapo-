from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.lista_productosInicio, name='lista_productos'),
    path('comprar/<int:producto_id>/', views.comprar, name='comprar'),
    path('historico/', views.historial_compras, name='historico_compras'),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('lista_productos/', views.lista_productos, name='lista_productos'),
    path('crear_producto/', views.crear_producto, name='crear_producto'),
    path('editar_producto/<int:producto_id>/', views.editar_producto, name='editar_producto'),
    path('lista_ventas/', views.lista_ventas, name='lista_ventas'),
]


