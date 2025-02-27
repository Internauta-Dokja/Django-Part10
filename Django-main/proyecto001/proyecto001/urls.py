"""
URL configuration for proyecto001 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings

from miapp import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name = "index"),
    path('inicio/', views.index, name = "inicio"),
    path('saludo/',views.saludo, name = "saludo"),
    path('rango/',views.rango,name="rango"),
    path('rango2/',views.rango2,name="rango2"),
    path('rango2/<int:a>',views.rango2,name="rango2"),
    path('rango2/<int:a>/<int:b>',views.rango2,name="rango2"),
    path('save-articulo/',views.save_articulo, name='save_articulo'),
    path('create-articulo/',views.create_articulo, name='create_articulo'),
    path('crear-articulo/<str:titulo>/<str:contenido>/<str:publicado>',views.crear_articulo,name="crear_articulo"),  
    path('buscar-articulo', views.buscar_articulo, name="buscar_articulo"),
    path('editar-articulo/<int:id>',views.editar_articulo,name="editar_articulo"),  
    path('listar-articulos/',views.listar_articulos,name="listar_articulos"),
    path('eliminar-articulo/<int:id>',views.eliminar_articulo, name='eliminar_articulo'),
    path('create-full-articulo/',views.create_full_articulo, name='create_full_articulo'),


]

# Configuración para cargar imágenes
if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



