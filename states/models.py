from django.db import models

class State(models.Model):
    name = models.CharField(max_length=100)
    abbrev = models.CharField(max_length=2)
    population = models.IntegerField(default=0)

    def __str__(self):
        return self.name

class City(models.Model):
    name = models.CharField(max_length=100)
    abbrev = models.CharField(max_length=3)
    population = models.IntegerField(default=0)
    state = models.ForeignKey(State, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'cities'

    def __str__(self):
        return self.name

