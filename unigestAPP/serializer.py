from rest_framework import serializers
from .models import Parent, Classe, Matiere, Etudiant, Evaluation, Professeur, EmploiDuTemps, AbsenceRetard, Filiere

class FiliereSerializer(serializers.ModelSerializer):
    class Meta:
        model = Filiere
        fields = "__all__"


class ClasseSerializer(serializers.ModelSerializer):
    filiere = FiliereSerializer(read_only=True)  # détail de la filière

    class Meta:
        model = Classe
        fields = "__all__"


class ParentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parent
        fields = "__all__"


class EtudiantSerializer(serializers.ModelSerializer):
    parent = ParentSerializer(read_only=True)   # détail du parent
    classe = ClasseSerializer(read_only=True)   # détail de la classe

    class Meta:
        model = Etudiant
        fields = "__all__"


class MatiereSerializer(serializers.ModelSerializer):
    filiere = FiliereSerializer(read_only=True)  # détail de la filière

    class Meta:
        model = Matiere
        fields = "__all__"


class ProfesseurSerializer(serializers.ModelSerializer):
    matieres = MatiereSerializer(many=True, read_only=True)  # liste des matières enseignées

    class Meta:
        model = Professeur
        fields = "__all__"


class EvaluationSerializer(serializers.ModelSerializer):
    etudiant = EtudiantSerializer(read_only=True)  # détail étudiant
    matiere = MatiereSerializer(read_only=True)    # détail matière

    class Meta:
        model = Evaluation
        fields = "__all__"


class EmploiDuTempsSerializer(serializers.ModelSerializer):
    classe = ClasseSerializer(read_only=True)    # détail classe
    matiere = MatiereSerializer(read_only=True)  # détail matière

    class Meta:
        model = EmploiDuTemps
        fields = "__all__"


class AbsenceRetardSerializer(serializers.ModelSerializer):
    etudiant = EtudiantSerializer(read_only=True)  # détail étudiant
    matiere = MatiereSerializer(read_only=True)    # détail matière

    class Meta:
        model = AbsenceRetard
        fields = "__all__"
