from django.contrib import admin

# Register your models here.

from .models import Zoo, Exhibit, Neighbor, Animal

class ZooAdmin(admin.ModelAdmin):
    list_display = ('name', 'id')

admin.site.register(Zoo, ZooAdmin)

class ExhibitAdmin(admin.ModelAdmin):
    list_display = ('name', 'id')

admin.site.register(Exhibit, ExhibitAdmin)

class NeighborAdmin(admin.ModelAdmin):
    list_display = ('fromExhibit', 'direction', 'toExhibit')

admin.site.register(Neighbor, NeighborAdmin)

class AnimalAdmin(admin.ModelAdmin):
    list_display = ('name', 'image', 'sound', 'food', 'political')

admin.site.register(Animal, AnimalAdmin)
