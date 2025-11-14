from django.urls import path, include
from . import views

urlpatterns = [

    path('/adoptar', views.contacto, name='adoptar'),

    path('/perros',views.vista_perros, name="perros"),
    path('/gatos',views.vista_gatos, name="gatos"),

]
