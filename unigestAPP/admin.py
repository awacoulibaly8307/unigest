from django.contrib import admin
from .models import Parent,Classe,Matiere,Etudiant,Filiere,Evaluation,Professeur,EmploiDuTemps,AbsenceRetard

# Register your models here.
admin.site.register(Parent)
admin.site.register(Classe)
admin.site.register(Matiere)
admin.site.register(Etudiant)
admin.site.register(Evaluation)
admin.site.register(Professeur)
admin.site.register(EmploiDuTemps)
admin.site.register(AbsenceRetard)
admin.site.register(Filiere)
