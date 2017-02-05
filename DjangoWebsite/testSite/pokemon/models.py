from django.db import models
from django.contrib.postgres.fields import JSONField

# Create your models here.
class Pokemon(models.Model):
    """Model that respresents pokemon."""
    name = models.CharField(max_length=30)
    egg_groups = JSONField()
    national_dex = models.IntegerField()
    types = JSONField()
    resistences = JSONField()
    weaknesses = JSONField()
    immunities = JSONField()
    abilities = JSONField()
    stage = models.CharField(max_length=10)
    hitpoints = models.IntegerField()
    attack = models.IntegerField()
    defense = models.IntegerField()
    special_attack = models.IntegerField()
    special_defense = models.IntegerField()
    speed = models.IntegerField()
    evs = models.CharField(max_length=10)
    generation = models.IntegerField()

class Type(models.Model):
    """Model that represents a type."""
    name = models.CharField(max_length=30)
    resistences = JSONField()
    weaknesses = JSONField()
    immunities = JSONField()

class Move(models.Model):
    """Model that represents a move."""
    name = models.CharField(max_length=50)
    atk_type = models.CharField(max_length=20)
    base_power = models.IntegerField()
    base_accuracy = models.IntegerField()
    description = models.CharField(max_length=200)

class Nature(models.Model):
    """Model to represent a nature."""
    name = models.CharField(max_length=20)
    positive = models.CharField(max_length=10)
    negative = models.CharField(max_length=10)

class Ability(models.Model):
    """Model to represent an ability."""
    name = models.CharField(max_length=40)
    description = models.CharField(max_length=10000)
