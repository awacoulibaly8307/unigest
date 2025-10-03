from tkinter.font import names

from django.urls import path
from .api_views import (
    ParentView, SingleParentView,
    ClasseView, SingleClasseView,
    MatiereView, SingleMatiereView,
    EtudiantView, SingleEtudiantsView,
    EvaluationView, SingleEvaluationiew,
    ProfesseurView, SingleProfessuerView,
    EmploiDuTempsView, SingleEmploiDuTempsView,
    AbsanceRetardView, SingleAbsenceRetardView,
    FiliereView,       SingleFilieredView,
)
from .views import delete_parent,edit_evaluation,delete_evaluation,edit_emploi,edit_professeur,edit_etudiant,edit_absence,edit_matiere,delete_filiere,edit_classe,edit_filiere,edit_parent,delete_etudiant,delete_matiere,delete_professeur,delete_classe,delete_emploi,delete_absence

urlpatterns = [
    # Parents
    path('parents/', ParentView.as_view()),
    path('parents/<int:pk>', SingleParentView.as_view()),
    path('parents/<int:pk>/delete',delete_parent, name='delete_parent'),
    path('parents/<int:pk>/edit',edit_parent, name='edit_parent'),

    # Classes
    path('classes/', ClasseView.as_view()),
    path('classes/<int:pk>', SingleClasseView.as_view()),
    path('classes/<int:pk>/delete', delete_classe, name='delete_classe'),
    path('classes/<int:pk>/edit', edit_classe, name='edit_classe'),

    # Matières
    path('matieres/', MatiereView.as_view()),
    path('matieres/<int:pk>', SingleMatiereView.as_view()),
    path('matieres/<int:pk>/edit', edit_matiere, name ='edit_matiere'),
    path('matieres/<int:pk>/delete', delete_matiere, name ='delete_matiere'),

    # Étudiants
    path('etudiants/', EtudiantView.as_view()),
    path('etudiants/<int:pk>/', SingleEtudiantsView.as_view()),
    path('etudiants/<int:pk>/delete', delete_etudiant, name='delete_etudiant'),
    path('etudiants/<int:pk>/edit/', edit_etudiant, name='edit_etudiant'),

    # Évaluations
    path('evaluation/', EvaluationView.as_view()),
    path('evaluation/<int:pk>', SingleEvaluationiew.as_view(), name='evaluation-detail'),
    path('evaluation/<int:pk>/edit', edit_evaluation, name='edit_evaluation'),
    path('evaluation/<int:pk>/delete', delete_evaluation, name='delete_evaluation'),

    # Professeurs
    path('professeurs/', ProfesseurView.as_view()),
    path('professeurs/<int:pk>', SingleProfessuerView.as_view(), name='professeur-detail'),
    path('professeurs/<int:pk>/delete', delete_professeur, name='delete_professeur'),
    path('professeurs/<int:pk>/edit', edit_professeur, name='edit_professeur'),

    # Emploi du temps
    path('emploi/', EmploiDuTempsView.as_view(), name='emploi-list'),
    path('emploi/<int:pk>', SingleEmploiDuTempsView.as_view(), name='emploi-detail'),
    path('emploi/<int:pk>/delete', delete_emploi, name='delete_emploi'),
    path('emploi/<int:pk>/edit', edit_emploi, name='edit_emploi'),

    # Absences & Retards
    path('absences-retards/', AbsanceRetardView.as_view()),
    path('absences-retards/<int:pk>', SingleAbsenceRetardView.as_view(), name='absenceretard-detail'),
    path('absences-retards/<int:pk>/delete', delete_absence, name='delete_absence'),
    path('absences-retards/<int:pk>/edit', edit_absence, name='edit_absence'),

    # Fliere
    path('filieres/', FiliereView.as_view()),
    path('filieres/<int:pk>', SingleFilieredView.as_view()),
    path('filieres/<int:pk>/delete', delete_filiere, name='delete_filiere'),
    path('filieres/<int:pk>/edit', edit_filiere, name='edit_filiere'),

]
