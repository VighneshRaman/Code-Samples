from django.contrib import admin
from .models import Pokemon, Type, Move, Nature

# Register your models here.
admin.site.register(Pokemon)
admin.site.register(Type)
admin.site.register(Move)
admin.site.register(Nature)
