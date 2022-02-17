from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField

from pets.models import Address, Pet


class Shelter(models.Model):
    """Shelter for animals"""
    name = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True)
    address = models.ForeignKey(Address, on_delete=models.PROTECT)
    site = models.URLField(null=True, blank=True)
    email = models.EmailField(blank=True, null=True)
    phone = PhoneNumberField(unique=True, blank=True, null=True)

    class Meta:
        db_table = 'users_shelter'
        verbose_name = 'Shelter'
        verbose_name_plural = 'Shelters'

    def __str__(self):
        return f'Shelter name: {self.name}'


class User(AbstractUser):
    """Model user"""
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    avatar = models.URLField(blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    phone = PhoneNumberField(unique=True, blank=True, null=True)
    pet = models.ForeignKey(Pet, on_delete=models.PROTECT, related_name='users', blank=True, null=True)
    shelter = models.ForeignKey(Shelter, on_delete=models.PROTECT, related_name='users', blank=True, null=True)

    class Meta:
        db_table = 'users_user'
        verbose_name = 'User'
        verbose_name_plural = 'Users'
