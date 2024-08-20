from django import forms

class ClienteFormulario(forms.Form):
    nombre = forms.CharField(max_length=40)
    apellido = forms.CharField(max_length=40)
    email = forms.EmailField()
    direccion = forms.CharField(max_length=40)
    telefono = forms.CharField(max_length=40)

class ProductoFormulario(forms.Form):
    nombre = forms.CharField(max_length=40)
    descripcion = forms.CharField(max_length=40)
    precio = forms.IntegerField()
    stock = forms.IntegerField()
    categoria = forms.CharField(max_length=40)

class CategoriaFormulario(forms.Form):
    nombre = forms.CharField(max_length=40)

class Buscar(forms.Form):
    nombre = forms.CharField(max_length=40)