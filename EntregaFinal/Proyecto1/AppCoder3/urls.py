from django.urls import path
from AppCoder3.views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', inicio, name="Inicio"),
    path('login/',inicioSesion,name="Login"),
    path('register/',registro,name="Signup"),
    path('logout/',cerrar_sesion,name="Logout"),
    path('editar/',editar_usuario,name="EditarUsuario"),
    path('agregar/',agregarAvatar,name="Avatar"),

    path('cliente/', clientes,name="Clientes"), 
    path('proveedor/', proveedores, name="Proveedores"),
    path('tienda/', tiendas, name="Tiendas"),
    path('clienteformulario/', clienteformulario,name="ClienteFormulario"),
    path('tiendaformulario/', tiendaformulario,name="TiendaFormulario"),
    path('buscartienda/', busquedatienda,name="BuscarTiendas"),
    path('resultadostienda/', resultadotienda,name="ResultadosTiendas"),
    #CRUD de proveedores
    path("leerproveedores/",leer_proveedor, name="ProveedorLeer"),
    path('proveedorformulario/', proveedorformulario,name="ProveedorFormulario"),
    path('eliminarproveedores/<provnombre>/', eliminar_proveedor,name="EliminarProveedor"),
    path('editarproveedores/<provnombre>/', editar_proveedor,name="EditarProveedor"),
    #CRUD de clientes usando clases
    path("client/list/",ListaClientes.as_view(), name="ClientesLeer"),
    path("client/<int:pk>",DetalleCliente.as_view(), name="ClientesDetalle"),
    path("client/crear/",CrearCliente.as_view(), name="ClienteCrear"),
    path("client/actualizar/<int:pk>",ActualizarCliente.as_view(), name="ClientesEditar"),
    path("client/borrar/<int:pk>",BorrarCliente.as_view(), name="ClientesBorrar"),
]