from .models import Pokemon, Type, Move, Nature, Ability
from rest_framework import serializers

class PokemonSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Pokemon
        fields = (
            'name',
            'egg_groups',
            'national_dex',
            'types',
            'resistences',
            'weaknesses',
            'immunities',
            'stage',
            'hitpoints',
            'attack',
            'defense',
            'special_attack',
            'special_defense',
            'speed',
            'evs',
            'abilities',
            'generation'
        )

class TypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Type
        fields = ('name','resistences','weaknesses','immunities')

class MoveSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Move
        fields = ('name','atk_type','base_power','base_accuracy','description')

class NatureSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Nature
        fields = ('name','positive','negative')

class AbilitySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Ability
        fields = ('name','description')
