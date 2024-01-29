from django.shortcuts import render
from django.http import HttpResponse
from AppCoder3.models import *
from AppCoder3.forms import *
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

def inicioSesion(request):
    if(request.method == "POST"):
        form = AuthenticationForm(request, data = request.POST)

        if form.is_valid():
            
            usuario = form.cleaned_data.get("username")
            contra = form.cleaned_data.get("password")

            user =   authenticate(username = usuario, password = contra)

            if user:
                login(request,user)

                return render(request,"AppCoder3/inicio.html",{"mensaje":f"Bienvenido(a) {user}"})
        else:
            return render(request,"AppCoder3/inicio.html",{"mensaje": "Los datos son incorrectos"})
    else:

        form = AuthenticationForm()
    
    return render(request,"AppCoder3/login.html",{"formulario":form})
            

def registro(request):

    if request.method == "POST":

        form = UsuarioRegistro(request.POST)

        if form.is_valid():

            username = form.cleaned_data["username"]
            form.save()
            return render(request,"AppCoder3/inicio.html",{"mensaje":"Usuario creado"})
        
    else:
        form = UsuarioRegistro()

    return render(request,"AppCoder3/registro.html",{"formulario":form})

@login_required
def editar_usuario(request):

    usuario = request.user

    if request.method == "POST":
        form = FormularioEditar(request.POST)
        if form.is_valid():
            
            info = form.cleaned_data

            usuario.email = info["email"]
            usuario.set_password(info["password1"])
            usuario.first_name = info["first_name"]
            usuario.last_name = info["last_name"]

            usuario.save()

            return render(request,"AppCoder3/inicio.html")
    else:
        form = FormularioEditar(initial={
            "email": usuario.email,
            "first_name":usuario.first_name,
            "last_name":usuario.last_name
        })
    
    return render(request, "AppCoder3/editarPerfil.html",{"formulario":form,"usuario":usuario})

def cerrar_sesion(request):

    logout(request)
    return render(request, "AppCoder3/logout.html")

def inicio(request):
    
    return render(request,"AppCoder3/inicio.html")


@login_required
def agregarAvatar(request):
    if request.method == "POST":

        form = AvatarFormulario(request.POST,request.FILES)

        if form.is_valid():
            usuarioActual = User.objects.get(username = request.user)
            avatar = Avatar(usuario = usuarioActual, imagen = form.cleaned_data["imagen"] )
            avatar.save()
            return render(request,"AppCoder3/inicio.html")
    else:
        form = AvatarFormulario()
    return render(request,"AppCoder3/agregarAvatar.html",{"formulario":form})


def clientes(request):

    return render(request,"AppCoder3/cliente.html")

def proveedores(request):

    return render(request,"AppCoder3/proveedor.html")

def tiendas(request):

    return render(request,"AppCoder3/tienda.html")

@login_required
def clienteformulario(request):
    if request.method == "POST":
        
        formulario1 = ClienteFormulario(request.POST)

        if formulario1.is_valid():
            info = formulario1.cleaned_data
            cliente1 = clientes1(nombre=info["nombre"], apellido=info["apellido"],correo=info["correo"])
            cliente1.save()
        
            return render(request, "AppCoder3/inicio.html")
        
    else:
        formulario1 = ClienteFormulario()

    
    return render(request, "AppCoder3/cliente.html",{"form1":formulario1})

@login_required
def proveedorformulario(request):
    if request.method == "POST":
        
        formulario1 = ProveedorFormulario(request.POST)

        if formulario1.is_valid():
            info = formulario1.cleaned_data
            cliente1 = proveedores1(empresa=info["empresa"], nombreRL=info["nombreRL"],apellidoRL=info["apellidoRL"], correo_empresa=info["correo_empresa"])
            cliente1.save()
        
            return render(request, "AppCoder3/inicio.html")
        
    else:
        formulario1 = ProveedorFormulario()

    
    return render(request, "AppCoder3/proveedor.html",{"form2":formulario1})

@login_required
def tiendaformulario(request):
    if request.method == "POST":
        
        formulario1 = TiendaFormulario(request.POST)

        if formulario1.is_valid():
            info = formulario1.cleaned_data
            cliente1 = tiendas1(empresa=info["empresa"], tienda=info["tienda"],pais=info["pais"], provincia=info["provincia"], distrito=info["distrito"], direccion=info["direccion"])
            cliente1.save()
        
            return render(request, "AppCoder3/inicio.html")
        
    else:
        formulario1 = TiendaFormulario()

    
    return render(request, "AppCoder3/tienda.html",{"form3":formulario1})

@login_required
def busquedatienda(request):
    return render(request, "AppCoder3/inicio.html")

@login_required
def resultadotienda(request):
    if request.GET['empresa']:

        empresa = request.GET["empresa"]
        tienda = tiendas1.objects.filter(empresa__icontains=empresa)

        return render(request,"AppCoder3/inicio.html",{"tienda":tienda, "empresa":empresa})
    else:
        respuesta = "No ingresaste ningún dato"

    return HttpResponse(respuesta)

@login_required
def leer_proveedor(request):
    proveedor = proveedores1.objects.all
    contexto = {"proveedor":proveedor} #crea diccionario
    return render(request, "AppCoder3/leer_proveedor.html",contexto)

@login_required
def eliminar_proveedor(request,provnombre):
    proveedor = proveedores1.objects.get(empresa=provnombre)
    proveedor.delete()

    proveedores = proveedores1.objects.all()
    contexto = {"proveedor":proveedores}

    return render(request, "AppCoder3/leer_proveedor.html",contexto)

@login_required
def editar_proveedor(request, provnombre):
    proveedor = proveedores1.objects.get(empresa=provnombre)

    if request.method == "POST":
        
        formulario1 = ProveedorFormulario(request.POST)

        if formulario1.is_valid():
            info = formulario1.cleaned_data
            
            proveedor.empresa = info["empresa"]
            proveedor.nombreRL = info["nombreRL"]
            proveedor.apellidoRL = info["apellidoRL"]
            proveedor.correo_empresa = info["correo_empresa"]

            proveedor.save()
        
            return render(request, "AppCoder3/inicio.html")
        
    else:
        formulario1 = ProveedorFormulario(initial={"empresa":proveedor.empresa, "nombreRL":proveedor.nombreRL, "apellidoRL":proveedor.apellidoRL, "correo_empresa":proveedor.correo_empresa})

    
    return render(request, "AppCoder3/editarproveedor.html",{"form2":formulario1, "empresa":provnombre})

#Clientes

class ListaClientes(LoginRequiredMixin,ListView):

    model = clientes1

class DetalleCliente(LoginRequiredMixin,DetailView):

    model = clientes1

class CrearCliente(LoginRequiredMixin,CreateView):

    model = clientes1
    success_url = "/AppCoder3/client/list"
    fields = ["nombre","apellido","correo"]

class ActualizarCliente(LoginRequiredMixin,UpdateView):

    model = clientes1
    success_url = "/AppCoder3/client/list"
    fields = ["nombre","apellido","correo"]

class BorrarCliente(LoginRequiredMixin,DeleteView):

    model = clientes1
    success_url = "/AppCoder3/client/list"