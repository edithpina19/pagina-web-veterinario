from django.contrib import admin
from .models import Gato,Perro

class GatoAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

admin.site.register(Gato, GatoAdmin)

class PerroAdmin(admin.ModelAdmin):
    readonly_fields= ('created', 'updated')
admin.site.register(Perro, PerroAdmin)

# Register your models here.
