# Generated by Django 4.0.2 on 2022-02-20 18:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='shelter',
            options={'ordering': ['-id'], 'verbose_name': 'Shelter', 'verbose_name_plural': 'Shelters'},
        ),
        migrations.AlterModelOptions(
            name='user',
            options={'ordering': ['-id'], 'verbose_name': 'User', 'verbose_name_plural': 'Users'},
        ),
    ]