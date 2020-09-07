from django.db import models


class Car(models.Model):
    manufacturer = models.CharField(max_length=128)
    model = models.CharField(max_length=255)
    year = models.IntegerField()

    TRANSMISSION_CHOICES = (
        (0, 'механика'),
        (1, 'автомат'),
        (2, 'робот'),
    )
    transmission = models.SmallIntegerField(choices=TRANSMISSION_CHOICES)
    color = models.ForeignKey('Color', on_delete=models.DO_NOTHING)

    def __str__(self):
        return f'{self.manufacturer} {self.model} ({self.year}) ID:{self.pk}'

    def transmission_display(self):
        return self.TRANSMISSION_CHOICES[self.transmission][1]


class Color(models.Model):
    name = models.CharField(max_length=64)
    hex = models.CharField(max_length=7)

    def __str__(self):
        return f'{self.name}'
