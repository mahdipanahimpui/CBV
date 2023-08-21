from django.db import models

class Car(models.Model):
    name = models.CharField(max_length=128)
    owner = models.CharField(max_length=128)
    year = models.PositiveSmallIntegerField()

    def __str__(self  ):
        return self.name