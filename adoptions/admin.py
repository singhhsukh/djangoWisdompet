from django.contrib import admin

from .models import Pet,Hash

@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    list_display = ['name','species','breed','age','sex']


@admin.register(Hash)
class HashAdmin(admin.ModelAdmin):
    list_display = ['text','hash']