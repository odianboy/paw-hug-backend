import uuid

from django.db import models


class Health(models.Model):
    """Pet health status"""
    id = models.SmallAutoField(primary_key=True)
    name = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True)

    class Meta:
        db_table = 'pets_health'
        verbose_name = 'Health'
        verbose_name_plural = 'Healths'

    def __str__(self):
        return f'{self.name}'


class Breed(models.Model):
    """Pet breed"""
    id = models.SmallAutoField(primary_key=True)
    name = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True)

    class Meta:
        db_table = 'pets_breed'
        verbose_name = 'Breed'
        verbose_name_plural = 'Breeds'

    def __str__(self):
        return f'{self.name}'


class Address(models.Model):
    """Address where the pet is located"""
    id = models.SmallAutoField(primary_key=True)
    city = models.CharField(max_length=50)
    street = models.CharField(max_length=50)
    house_number = models.SmallIntegerField()
    description = models.TextField(null=True, blank=True)

    class Meta:
        db_table = 'pets_address'
        verbose_name = 'Address'
        verbose_name_plural = 'Addresses'

    def __str__(self):
        return f'{self.city}'


class Classification(models.Model):
    """Pet classification"""
    id = models.SmallAutoField(primary_key=True)
    name = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True)

    class Meta:
        db_table = 'pets_classification'
        verbose_name = 'Classification'
        verbose_name_plural = 'Classifications'

    def __str__(self):
        return f'{self.name}'


class Pet(models.Model):
    """Model pet"""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=25)
    birthday = models.DateField(blank=True, null=True)
    photo = models.URLField(blank=True, null=True)
    description = models.TextField(null=True, blank=True)
    is_home = models.BooleanField(default=False)
    classification = models.ForeignKey(Classification, on_delete=models.PROTECT, related_name='pets')
    health = models.ForeignKey(Health, on_delete=models.PROTECT, related_name='pets')
    bread = models.ForeignKey(Breed, on_delete=models.PROTECT, related_name='pets')
    address = models.ForeignKey(Address, on_delete=models.PROTECT, related_name='pets')

    class Meta:
        db_table = 'pets_pet'
        verbose_name = 'Pet'
        verbose_name_plural = 'Pets'

    def __str__(self):
        return f'{self.name}'
