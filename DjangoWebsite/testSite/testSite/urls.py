"""testSite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from rest_framework import routers
# from home.views import UserViewSet, GroupViewSet
# from pokemon.views import PokemonViewSet, TypeViewSet, MoveViewSet, NatureViewSet, AbilityViewSet

admin.autodiscover()

# Routers
router = routers.DefaultRouter()
# router.register(r'users', UserViewSet)
# router.register(r'groups', GroupViewSet)
# router.register(r'pkmn/pokemon', PokemonViewSet)
# router.register(r'pkmn/types', TypeViewSet)
# router.register(r'pkmn/moves', MoveViewSet)
# router.register(r'pkmn/natures', NatureViewSet)
# router.register(r'pkmn/abilities', AbilityViewSet)

urlpatterns = [
    url(r'^', include('home.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include(router.urls)),
]
