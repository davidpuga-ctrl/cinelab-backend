"""
URL configuration for backend_cine project.

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
from django.urls import path, include
from django.conf import settings             # <--- Para saber dónde guardar fotos
from django.conf.urls.static import static   # <--- Para poder ver las fotos
from rest_framework.routers import DefaultRouter
from catalogo.views import DirectorViewSet, PeliculaViewSet

# 1. Configuración de la API (Esto ya lo tenías bien)
router = DefaultRouter()
router.register(r'directores', DirectorViewSet)
router.register(r'peliculas', PeliculaViewSet)

# 2. Lista de Rutas
urlpatterns = [
    path('admin/', admin.site.urls),
    path('o/', include('oauth2_provider.urls', namespace='oauth2_provider')), # OAuth
    path('api/', include(router.urls)), # Conectamos el router aquí
]

# 3. Magia para las Imágenes (Solo funciona en modo DEBUG)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)