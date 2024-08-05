from django.core.validators import MinValueValidator, RegexValidator, MinLengthValidator
from django.db import models

from main_app.choices import StatusChoices
from main_app.managers import AstronautManager


# Create your models here.
class Astronaut(models.Model):
    name = models.CharField(
        max_length=120,
        validators=[MinLengthValidator(2)]
    )

    phone_number = models.CharField(
        max_length=15,
        validators=[
            RegexValidator(regex=r'^\d+$')
        ],
        unique=True
    )

    is_active = models.BooleanField(default=True)
    date_of_birth = models.DateField(null=True, blank=True)
    spacewalks = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    updated_at = models.DateTimeField(auto_now=True)

    objects = AstronautManager()


class Spacecraft(models.Model):
    name = models.CharField(
        max_length=120,
        validators=[MinLengthValidator(2)]
    )

    manufacturer = models.CharField(max_length=100)
    capacity = models.PositiveSmallIntegerField(validators=[MinValueValidator(1)])
    weight = models.FloatField(validators=[MinValueValidator(0.0)])
    launch_date = models.DateField()
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Mission(models.Model):
    name = models.CharField(
        max_length=120,
        validators=[MinLengthValidator(2)]
    )

    description = models.TextField(null=True, blank=True)
    status = models.CharField(max_length=9, choices=StatusChoices, default="Planned")
    launch_date = models.DateField()
    updated_at = models.DateTimeField(auto_now=True)

    spacecraft = models.ForeignKey(
        'Spacecraft',
        on_delete=models.CASCADE,
        related_name='missions'
    )

    astronauts = models.ManyToManyField('Astronaut', related_name='missions')
    commander = models.ForeignKey(
        'Astronaut',
        on_delete=models.SET_NULL,
        related_name='commanders',
        null=True,
        blank=True)