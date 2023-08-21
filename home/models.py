from django.db import models

class Car(models.Model):
    name = models.CharField(max_length=128)
    owner = models.CharField(max_length=128)
    year = models.PositiveSmallIntegerField()
    created = models.DateTimeField(null=True, blank=True, auto_now_add=True)

    def __str__(self  ):
        return self.name