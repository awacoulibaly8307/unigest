from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('index/', index, name='index'),
    path('absence/', absence, name='absence'),
    path('classe/', classe, name='classe'),
    path('emploi/', emploi, name='emploi'),
    path('etudiant/', etudiant, name='etudiant'),
    path('matiere/', matiere, name='matiere'),
    path('professeur/', professeur, name='professeur'),
    path('parent/', parent, name='parent'),

]

