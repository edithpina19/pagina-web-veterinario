from django.db import models

class Perro(models.Model):
    nombre=models.CharField(max_length= 50)
    raza=models.CharField(max_length= 50)
    imagen=models.ImageField()
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name='perro'
        verbose_name_plural='perros'

    def __str__(self):
        return self.nombre

class Gato(models.Model):
    nombre=models.CharField(max_length=50)
    raza=models.CharField(max_length=50)
    imagen=models.ImageField(upload_to='adopciones')
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name='gato'
        verbose_name_plural='gatos'

    def __str__(self):
        return self.nombre





# Create your models here.
