# users/admin.py
from django.contrib import admin

from .models import Pegadri, Cocodri, Functionteam


@admin.register(Pegadri)
class PegadriAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'owner']


@admin.register(Cocodri)
class CocodriAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'owner']


@admin.register(Functionteam)
class FunctionteamAdmin(admin.ModelAdmin):
    list_display = ['name']