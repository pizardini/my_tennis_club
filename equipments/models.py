from django.db import models


class Equipment(models.Model):
    ball = models.IntegerField(null=True)
    racket = models.IntegerField(null=True)



