from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import generics
from .models import Pokemon, Type, Move, Nature, Ability
from .serializers import PokemonSerializer, TypeSerializer, MoveSerializer, NatureSerializer, AbilitySerializer

# API Serializers
class PokemonViewSet(viewsets.ModelViewSet):
    """API endpoint that allows Pokemon to be viewed or edited."""
    queryset = Pokemon.objects.all()
    serializer_class = PokemonSerializer

class TypeViewSet(viewsets.ModelViewSet):
    """API endpoint that allows Type to be viewed or edited."""
    queryset = Type.objects.all()
    serializer_class = TypeSerializer

class MoveViewSet(viewsets.ModelViewSet):
    """API endpoint that allows Move to be viewed or edited."""
    queryset = Move.objects.all()
    serializer_class = MoveSerializer

class NatureViewSet(viewsets.ModelViewSet):
    """API endpoint that allows Nature to be viewed or edited."""
    queryset = Nature.objects.all()
    serializer_class = NatureSerializer

class AbilityViewSet(viewsets.ModelViewSet):
    """API endpoint that allows Ability to be viewed or edited"""
    queryset = Ability.objects.all()
    serializer_class = AbilitySerializer

# Create your views here.
