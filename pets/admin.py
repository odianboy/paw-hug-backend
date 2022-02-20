from django.contrib import admin

from .models import (
    Health,
    Breed,
    Address,
    Classification,
    Pet
)


@admin.register(Health)
class AdminHealth(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'description',
    )
    list_filter = (
        'name',
    )
    search_fields = ('name',)
    list_display_links = ('name',)
    exclude = ['id']


@admin.register(Breed)
class AdminBreed(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'description',
    )
    list_filter = (
        'name',
    )
    search_fields = ('name',)
    list_display_links = ('name',)
    exclude = ['id']


@admin.register(Address)
class AdminAddress(admin.ModelAdmin):
    list_display = (
        'id',
        'city',
        'street',
        'house_number',
        'description',
    )
    list_filter = (
        'city',
    )
    search_fields = ('city',)
    list_display_links = ('city',)
    exclude = ['id']


@admin.register(Classification)
class AdminClassification(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'description',
    )
    list_filter = (
        'name',
    )
    search_fields = ('name',)
    list_display_links = ('name',)
    exclude = ['id']


@admin.register(Pet)
class AdminPet(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'birthday',
        'is_home',
        'publication_date',
    )
    list_filter = (
        'name',
    )
    search_fields = ('name',)
    list_display_links = ('name',)
    exclude = ['id']
