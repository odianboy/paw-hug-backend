from django.contrib import admin
from django.contrib.auth.models import Group

from .models import Shelter, User

admin.site.unregister([Group])


@admin.register(Shelter)
class AdminHealth(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'site',
        'phone',
    )
    list_filter = (
        'name',
    )
    search_fields = ('name',)
    list_display_links = ('name',)
    exclude = ['id']


@admin.register(User)
class AdminUser(admin.ModelAdmin):
    list_display = (
        'id',
        'username',
        'first_name',
        'phone',
    )
    list_filter = (
        'first_name',
    )
    search_fields = ('first_name',)
    list_display_links = ('username', )
    exclude = ['id']
