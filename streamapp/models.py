from django.db import models

# Create your models here.

class familia(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, verbose_name='Nombre')
    apellido = models.CharField(max_length=100, verbose_name='Apellido')
    imagen = models.ImageField(upload_to='imagenes/', verbose_name='Imagen', null=True)
   
    def _str_(self):
        fila="Nombre: " + self.nombre + " - " + "Apellido: " + self.apellido
        return fila

    def delete(self, using=None, keep_parents=False):
        self.imagen.storage.delete(self.imagen.name)
        super().delete()


