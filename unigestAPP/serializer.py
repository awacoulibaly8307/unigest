from rest_framework import serializers
from .models import Parent,Classe,Matiere,Etudiant,Evaluation,Professeur,EmploiDuTemps,AbsenceRetard



class ParentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parent
        fields = '_all_'

class ClasseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classe
        fields = '_all_'

class MatiereSerializer(serializers.ModelSerializer):
    class Meta:
        model = Matiere
        fields = '_all_'

class EtudiantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Etudiant
        fields = '_all_'

class EvaluationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Evaluation
        fields = '_all_'

class ProfesseurSerializer(serializers.ModelSerializer):
    class Meta:
        model = Professeur
        fields = '_all_'

class EmploiDuTempsSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmploiDuTemps
        fields = '_all_'

class AbsenceRetardSerializer(serializers.ModelSerializer):
    class Meta:
        model = AbsenceRetard
        fields = '_all_'
        

