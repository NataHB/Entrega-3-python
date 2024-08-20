from mi_app import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('productos/', views.resultado_busqueda, name='productos'),
    path('buscar/', views.formularios_combinados, name='buscar'),
]