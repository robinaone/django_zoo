from django.urls import path

from . import views

urlpatterns = [
    path('', views.ZooListView.as_view(), name='zooList'),
    path('<int:pk>', views.ZooDetailView.as_view(), name='zooDetail'),
    path('exhibit/<int:pk>', views.ExhibitDetailView.as_view(), name='exhibitDetail'),
    path('animal/<int:pk>', views.AnimalDetailView.as_view(), name='animalDetail'),
    path('aboutus', views.aboutus, name='aboutus'),
    path('contactus', views.contactus, name='contactus'),
]
