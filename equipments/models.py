from django.db import models
from enum import Enum


class EquipmentType(Enum):
    BALL = 'ball'
    RACKET = 'racket'


class Equipment(models.Model):
    type = models.CharField(max_length=10, choices=[(tag.value, tag.name) for tag in EquipmentType])
    serial = models.CharField(max_length=50, null=True)
    brand = models.CharField(max_length=100, blank=True)
    model = models.CharField(max_length=100, blank=True)
    purchase_date = models.DateField(null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return f"{self.type.upper()} - {self.serial}"



