from django.shortcuts import render, redirect
from mi_app.models import Categoria, Producto, Cliente
from mi_app.forms import ClienteFormulario, ProductoFormulario, CategoriaFormulario

def index(req):
    return render(req, 'mi_app/index.html')

def about(req):
    return render(req, 'mi_app/about.html')

def resultado_busqueda(req):
    nombre = req.GET.get('nombre', '')  # Captura el parámetro 'nombre', o una cadena vacía si no existe
    if nombre:
        categorias = Categoria.objects.filter(nombre__icontains=nombre)  # Filtra las categorías por nombre
    else:
        categorias = ''

    return render(req, 'mi_app/productos.html', {'categorias': categorias})



def formularios_combinados(req):
    if req.method == 'POST':
        cliente_form = ClienteFormulario(req.POST, prefix='cliente') 
        producto_form = ProductoFormulario(req.POST, prefix='producto')
        categoria_form = CategoriaFormulario(req.POST, prefix='categoria')

        if cliente_form.is_valid():
            informacion = cliente_form.cleaned_data
            cliente = Cliente(
                nombre=informacion['nombre'],
                apellido=informacion['apellido'],
                email=informacion['email'],
                direccion=informacion['direccion'],
                telefono=informacion['telefono'],
            )
            cliente.save()

        if producto_form.is_valid():
            informacion = producto_form.cleaned_data
            producto = Producto(
                nombre=informacion['nombre'],
                descripcion=informacion['descripcion'],
                precio=informacion['precio'],
                stock=informacion['stock'],
                categoria=informacion['categoria'],
            )
            producto.save()

        if categoria_form.is_valid():
            informacion = categoria_form.cleaned_data
            categoria = Categoria(
                nombre=informacion['nombre'],
            )
            categoria.save()

        return redirect('index')  # Redirigir a la página de inicio

    else:
        cliente_form = ClienteFormulario(prefix='cliente')
        producto_form = ProductoFormulario(prefix='producto')
        categoria_form = CategoriaFormulario(prefix='categoria')

    return render(req, 'mi_app/buscar.html', {
        'cliente_form': cliente_form,
        'producto_form': producto_form,
        'categoria_form': categoria_form,
    })

