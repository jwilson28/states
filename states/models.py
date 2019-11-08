from django.db import models
from django.contrib.auth.models import User


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


class Activity(models.Model):
    SR = "sports and recreation"
    ED = "education"
    HE = "health"
    FOOD = "food"
    ADMIN = "admin"
    WRK = "work"

    ACTIVITY_TYPE_CHOICES = [
    (SR, "sports and recreation"),
    (ED, "education"),
    (HE,"health"),
    (FOOD, "food"),
    (ADMIN,"admin"),
    (WRK, "work"),
    ]
    name = models.CharField(max_length=100)
    date = models.DateTimeField('date of event')
    location = models.ForeignKey(City, on_delete=models.CASCADE)
    participants = models.ManyToManyField(User)
    activity_type = models.CharField(max_length=100, choices=ACTIVITY_TYPE_CHOICES)

    class Meta:
        verbose_name_plural = 'activities'
        