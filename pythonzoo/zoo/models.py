from django.db import models

# Create your models here.

from django.urls import reverse

class Zoo(models.Model):
    name = models.CharField(max_length=200, help_text="Enter a Zoo name.")
    logoFileName = models.CharField(max_length=200, help_text="Enter a url.", null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('zooDetail', args=[str(self.id)])

class Exhibit(models.Model):
    name = models.CharField(max_length=200, help_text="Enter an Exhibit name.")
    zoo = models.ForeignKey('Zoo', on_delete=models.SET_NULL, null=True)
    hasExit = models.BooleanField(default=False)
    #animal = models.ForeignKey('Animal', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('exhibitDetail', args=[str(self.id)])

    def getZooName(self):
        return self.zoo.name

class Neighbor(models.Model):
    fromExhibit = models.ForeignKey('Exhibit', on_delete=models.SET_NULL, null=True, related_name='fromExhibit')
    toExhibit = models.ForeignKey('Exhibit', on_delete=models.SET_NULL, null=True, related_name='toExhibit')
    CARDINAL = (
        ('n', 'North'),
        ('s', 'South'),
        ('w', 'West'),
        ('e', 'East'),
        ('ne', 'Northeast'),
        ('nw', 'Northwest'),
        ('se', 'Southeast'),
        ('sw', 'Southwest')
    )
    direction = models.CharField(max_length=2, choices=CARDINAL, help_text="Enter direction", null=True, blank=True)


    def __str__(self):
        return str(self.fromExhibit) + ': ' + str(self.direction) + ' to: ' + str(self.toExhibit)

class Animal(models.Model):
    name = models.CharField(max_length=200)
    imageFileName = models.CharField(max_length=200, null=True)
    sound = models.CharField(max_length=200)
    food = models.CharField(max_length=200)
    political = models.CharField(max_length=200)
    exhibit = models.ForeignKey('Exhibit', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('animalDetail', args=[str(self.id)])
