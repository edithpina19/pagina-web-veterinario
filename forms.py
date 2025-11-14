from django import forms

class FormularioAdoptar(forms.Form):
    nombreadoptar=forms.CharField(label="Nombre de la mascota a adoptar", required=True)
    nombre=forms.CharField(label="Nombre", required=True)
    email= forms.CharField(label="Email", required=True)
    num= forms.CharField(label="Num. De Telefono", required=True)
    direccion= forms.CharField(label="Direccion", required=True)