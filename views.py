from django.shortcuts import render
from .forms import FormularioAdoptar

def vista_perros(request):
    return render(request, 'adopciones/perros.html')

def vista_gatos(request):
    return render(request, 'adopciones/gatos.html')

def contacto(request):
    formulario_adoptar = FormularioAdoptar()
    return render(request, "adopciones/adoptar.html", {'Formulario': formulario_adoptar})

# Create your views here.
