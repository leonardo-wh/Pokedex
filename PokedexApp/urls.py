from django.conf.urls import url, include
from django.conf.urls.static import static

from PokedexApp.views import index, ver_pokemon, tipo_pokemon

from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
   url(r'^$', index, name='index'),
   url(r'^verpokemon/(?P<pk>\d+)$', ver_pokemon, name='ver_pokemon'),
   url(r'^tipopokemon/(?P<types>[-\w]+)$', tipo_pokemon, name='tipo_pokemon'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
