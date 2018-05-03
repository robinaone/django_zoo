from django.contrib import admin

# Register your models here.

from .models import Zoo, Exhibit, Neighbor, Animal

class ZooAdmin(admin.ModelAdmin):
    list_display = ('name', 'id', 'logoFileName', 'get_absolute_url')

admin.site.register(Zoo, ZooAdmin)

class ExhibitAdmin(admin.ModelAdmin):
    list_display = ('name', 'id', 'get_absolute_url')

admin.site.register(Exhibit, ExhibitAdmin)

class NeighborAdmin(admin.ModelAdmin):
    list_display = ('id', 'fromExhibit', 'direction', 'toExhibit')

admin.site.register(Neighbor, NeighborAdmin)

class AnimalAdmin(admin.ModelAdmin):
    list_display = ('name', 'id', 'exhibit', 'get_absolute_url')

admin.site.register(Animal, AnimalAdmin)
