# Generated by Django 5.0.4 on 2024-07-02 21:22

from django.db import migrations


def set_salary(apps, schema_editor):
    MULTIPLIER = 120

    smartphone_mode = apps.get_model('main_app', 'Smartphone')

    for smartphone in smartphone_mode.objects.all():
        smartphone.price = MULTIPLIER * len(smartphone.brand)
        smartphone.save()


def set_category(apps, schema_editor):
    smartphone_mode = apps.get_model('main_app', 'Smartphone')

    for smartphone in smartphone_mode.objects.all():
        if smartphone.price > 750:
            smartphone.category = 'Expensive'
        else:
            smartphone.category = 'Cheap'

        smartphone.save()

def reverse_fulling_of_columns(apps, schema_editor):
    smartphone_model = apps.get_model('main_app', 'Smartphone')

    for smartphone in smartphone_model.objects.all():
        smartphone.price = smartphone_model._meta.get_field('price').default
        smartphone.category = smartphone_model._meta.get_field('category').default
        smartphone.save()


def set_all_columns(apps, schema_editor):
    set_salary(apps, schema_editor)
    set_category(apps, schema_editor)


class Migration(migrations.Migration):
    dependencies = [
        ('main_app', '0011_smartphone'),
    ]

    operations = [
        migrations.RunPython(set_all_columns, reverse_fulling_of_columns),
    ]
