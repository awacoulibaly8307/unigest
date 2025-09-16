from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('index/', index, name='index'),
    path('absences-retards/', absence, name='absences-retards'),
    path('classes/', classe, name='classes'),
    path('emplois/', emploi, name='emplois'),
    path('etudiants/', etudiant, name='etudiants'),
    path('matieres/', matiere, name='matieres'),
    path('professeurs/', professeur, name='professeurs'),
    path('parents/', parent, name='parents'),
    path('filieres/', filiere, name='filieres'),
]