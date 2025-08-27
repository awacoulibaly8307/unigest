from django.urls import path
from .api_views import (
    ParentView, SingleParentView,
    ClasseView, SingleClasseView,
    MatiereView, SingleMatiereView,
    EtudiantView, SingleEtudiantView,
    EvaluationView, SingleEvaluationiew,
    ProfesseurView, SingleProfessuerView,
    EmploiDuTempsView, SingleEmploiDuTempsView,
    AbsanceRetardView, SingleAbsenceRetardView
)

urlpatterns = [
    # Parents
    path('parents/', ParentView.as_view(), name='parent-list'),
    path('parents/<int:pk>/', SingleParentView.as_view(), name='parent-detail'),

    # Classes
    path('classes/', ClasseView.as_view(), name='classe-list'),
    path('classes/<int:pk>/', SingleClasseView.as_view(), name='classe-detail'),

    # Matières
    path('matieres/', MatiereView.as_view(), name='matiere-list'),
    path('matieres/<int:pk>/', SingleMatiereView.as_view(), name='matiere-detail'),

    # Étudiants
    path('etudiants/', EtudiantView.as_view(), name='etudiant-list'),
    path('etudiants/<int:pk>/', SingleEtudiantView.as_view(), name='etudiant-detail'),

    # Évaluations
    path('evaluations/', EvaluationView.as_view(), name='evaluation-list'),
    path('evaluations/<int:pk>/', SingleEvaluationiew.as_view(), name='evaluation-detail'),

    # Professeurs
    path('professeurs/', ProfesseurView.as_view(), name='professeur-list'),
    path('professeurs/<int:pk>/', SingleProfessuerView.as_view(), name='professeur-detail'),

    # Emploi du temps
    path('emplois/', EmploiDuTempsView.as_view(), name='emploi-list'),
    path('emplois/<int:pk>/', SingleEmploiDuTempsView.as_view(), name='emploi-detail'),

    # Absences & Retards
    path('absences-retards/', AbsanceRetardView.as_view(), name='absenceretard-list'),
    path('absences-retards/<int:pk>/', SingleAbsenceRetardView.as_view(), name='absenceretard-detail'),
]
