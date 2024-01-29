from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class clientes1(models.Model):
    def __str__(self) -> str:
        return f"Nombre completo: {self.nombre} {self.apellido} ------ Correo:{self.correo}"
    

    nombre = models.CharField(max_length = 60)
    apellido = models.CharField(max_length = 60)
    correo = models.EmailField()
    
class proveedores1(models.Model):
    def __str__(self) -> str:
        return f"Empresa: {self.empresa} ------ Representante Legal :{self.nombreRL}"
    

    empresa = models.CharField(max_length = 60)
    nombreRL = models.CharField(max_length = 60)
    apellidoRL = models.CharField(max_length = 60)
    correo_empresa = models.EmailField()

class tiendas1(models.Model):
    def __str__(self) -> str:
        return f"Empresa: {self.empresa} ------ Tienda :{self.tienda}"


    empresa = models.CharField(max_length=60)
    tienda = models.CharField(max_length=60)
    pais = models.CharField(max_length = 60)
    provincia = models.CharField(max_length = 60)
    distrito = models.CharField(max_length = 60)
    direccion = models.CharField(max_length = 60)

class Avatar(models.Model):
    usuario = models.ForeignKey(User, on_delete = models.CASCADE)
    imagen = models.ImageField(upload_to="avatares", null=True, blank=True)

