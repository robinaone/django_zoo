from django.shortcuts import render
from django.views import generic

from.models import Zoo, Exhibit, Animal

# Create your views here.

def aboutus(request):
    return render(
        request,
        "zoo/aboutus.html",
        context = { },
    )

def contactus(request):
    return render(
        request,
        "zoo/contactus.html",
        context = { },
    )

class ZooListView(generic.ListView):
    model = Zoo

class ZooDetailView(generic.DetailView):
    model = Zoo

class ExhibitDetailView(generic.DetailView):
    model = Exhibit

class AnimalDetailView(generic.DetailView):
    model = Animal
