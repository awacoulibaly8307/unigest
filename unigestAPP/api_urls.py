from tkinter.font import names

from django.urls import path
from .api_views import (
    ParentView, SingleParentView,
    ClasseView, SingleClasseView,
    MatiereView, SingleMatiereView,
    EtudiantView, SingleEtudiantView,
    EvaluationView, SingleEvaluationiew,
    ProfesseurView, SingleProfessuerView,
    EmploiDuTempsView, SingleEmploiDuTempsView,
    AbsanceRetardView, SingleAbsenceRetardView,
    FiliereView,       SingleFilieredView,
)
from .views import delete_parent,delete_filiere,delete_etudiant,delete_matiere,delete_professeur,delete_classe,delete_emploi,delete_absence

urlpatterns = [
    # Parents
    path('parents/', ParentView.as_view()),
    path('parents/<int:pk>', SingleParentView.as_view()),
    path('parents/<int:pk>/delete',delete_parent, name='delete_parent'),

    # Classes
    path('classes/', ClasseView.as_view()),
    path('classes/<int:pk>', SingleClasseView.as_view()),
    path('classes/<int:pk>/delete', delete_classe, name='delete_classe'),

    # Matières
    path('matieres/', MatiereView.as_view()),
    path('matieres/<int:pk>', SingleMatiereView.as_view()),
    path('matieres/<int:pk>/delete', delete_matiere, name ='delete_matiere'),

    # Étudiants
    path('etudiants/', EtudiantView.as_view(), name='etudiant-list'),
    path('etudiants/<int:pk>', SingleEtudiantView.as_view(), name='etudiant-detail'),
    path('etudiants/<int:pk>/delete', delete_etudiant, name='delete_etudiant'),

    # Évaluations
    path('evaluations/', EvaluationView.as_view(), name='evaluation-list'),
    path('evaluations/<int:pk>/', SingleEvaluationiew.as_view(), name='evaluation-detail'),

    # Professeurs
    path('professeurs/', ProfesseurView.as_view(), name='professeur-list'),
    path('professeurs/<int:pk>', SingleProfessuerView.as_view(), name='professeur-detail'),
    path('professeurs/<int:pk>/delete', delete_professeur, name='delete_professeur'),

    # Emploi du temps
    path('emplois/', EmploiDuTempsView.as_view(), name='emploi-list'),
    path('emplois/<int:pk>', SingleEmploiDuTempsView.as_view(), name='emploi-detail'),
    path('emplois/<int:pk>/delete', delete_emploi, name='delete_emploi'),

    # Absences & Retards
    path('absences-retards/', AbsanceRetardView.as_view()),
    path('absences-retards/<int:pk>', SingleAbsenceRetardView.as_view(), name='absenceretard-detail'),
    path('absences-retards/<int:pk>/delete', delete_absence, name='delete_absence'),

    # Fliere
    path('filieres/', FiliereView.as_view()),
    path('filieres/<int:pk>', SingleFilieredView.as_view()),
    path('filieres/<int:pk>/delete', delete_filiere, name='delete_filiere'),

]
