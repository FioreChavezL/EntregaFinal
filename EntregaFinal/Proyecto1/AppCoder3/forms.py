from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from AppCoder3.models import Avatar

class ClienteFormulario(forms.Form):
    
    nombre = forms.CharField(max_length = 60)
    apellido = forms.CharField(max_length = 60)
    correo = forms.EmailField()


class ProveedorFormulario(forms.Form):
    
    empresa = forms.CharField(max_length = 60)
    nombreRL = forms.CharField(max_length = 60)
    apellidoRL = forms.CharField(max_length = 60)
    correo_empresa = forms.EmailField()

class TiendaFormulario(forms.Form):
    empresa = forms.CharField(max_length=60)
    tienda = forms.CharField(max_length=60)
    pais = forms.CharField(max_length = 60)
    provincia = forms.CharField(max_length = 60)
    distrito = forms.CharField(max_length = 60)
    direccion = forms.CharField(max_length = 60)


class UsuarioRegistro(UserCreationForm):

    email = forms.EmailField()
    password1 = forms.CharField(label = "Contraseña", widget = forms.PasswordInput)
    password2 = forms.CharField(label = "Confirmar Contraseña", widget = forms.PasswordInput)

    class Meta:
        model = User
        fields = ["username","email","first_name","last_name","password1","password2"]


class FormularioEditar(UserCreationForm):

    email = forms.EmailField()
    password1 = forms.CharField(label = "Contraseña", widget = forms.PasswordInput)
    password2 = forms.CharField(label = "Confirmar Contraseña", widget = forms.PasswordInput)

    class Meta:
        model = User
        fields = ["email","first_name","last_name","password1","password2"]

class AvatarFormulario(forms.ModelForm):
    class Meta:
        model = Avatar
        fields = ["imagen"]