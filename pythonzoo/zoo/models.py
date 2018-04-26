from django.db import models

# Create your models here.

from django.urls import reverse

class Zoo(models.Model):
    name = models.CharField(max_length=200, help_text="Enter a Zoo name.")

    def __str__(self):
        return self.name

class Exhibit(models.Model):
    name = models.CharField(max_length=200, help_text="Enter an Exhibit name.")
    zoo = models.ForeignKey('Zoo', on_delete=models.SET_NULL, null=True)
    hasExit = models.BooleanField(default=False)
    animal = models.ForeignKey('Animal', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name

class Neighbor(models.Model):
    fromExhibit = models.ForeignKey('Exhibit', on_delete=models.SET_NULL, null=True)
    direction = models.CharField(max_length=200)
    toExhibit = models.ForeignKey('Exhibit', on_delete=models.SET_NULL, null=True, related_name='neighbor_of')

    def __str__(self):
        return str(self.fromExhibit) + ': ' + str(self.direction) + ' to: ' + str(self.toExhibit)

class Animal(models.Model):
    name = models.CharField(max_length=200)
    image = models.FileField()
    sound = models.CharField(max_length=200)
    food = models.CharField(max_length=200)
    political = models.CharField(max_length=200)

    def __str__(self):
        return self.name
