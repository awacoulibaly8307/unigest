from rest_framework import serializers
from .models import Parent, Classe, Matiere, Etudiant, Evaluation, Professeur, EmploiDuTemps, AbsenceRetard, Filiere


class ParentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parent
        fields = "__all__"

class ClasseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classe
        fields = "__all__"

class MatiereSerializer(serializers.ModelSerializer):
    class Meta:
        model = Matiere
        fields = "__all__"

class EtudiantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Etudiant
        fields = "__all__"

class EvaluationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Evaluation
        fields = "__all__"

class ProfesseurSerializer(serializers.ModelSerializer):
    class Meta:
        model = Professeur
        fields = "__all__"

class EmploiDuTempsSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmploiDuTemps
        fields = "__all__"

class AbsenceRetardSerializer(serializers.ModelSerializer):
    class Meta:
        model = AbsenceRetard
        fields = "__all__"

class FiliereSerializer(serializers.ModelSerializer):
    class Meta:
         model = Filiere
         fields = "__all__"

