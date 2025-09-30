from rest_framework import serializers
from .models import Parent, Classe, Matiere, Etudiant, Evaluation, Professeur, EmploiDuTemps, AbsenceRetard, Filiere

class FiliereSerializer(serializers.ModelSerializer):
    class Meta:
        model = Filiere
        fields = "__all__"


class ClasseSerializer(serializers.ModelSerializer):
    filiere_detail = FiliereSerializer(source='filiere', read_only=True)

    class Meta:
        model = Classe
        fields = [
            'id',
            'filiere_detail',
            'filiere',
            'nom',
            'description',
            'annee_universitaire'
        ]


class ParentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parent
        fields = "__all__"


class EtudiantSerializer(serializers.ModelSerializer):
    parent_detail = ParentSerializer(source='parent', read_only=True)
    classe_detail = ClasseSerializer(source='classe', read_only=True)

    class Meta:
        model = Etudiant
        fields = [
             'id',
            'parent',
            'parent_detail',
            'classe',
            'classe_detail',
            'motdepasse',
            'nom',
            'prenom',
            'sexe',
            'matricule',
            'dateNaissance',
            'adresse',
            'telephone',
            'email'
        ]


class MatiereSerializer(serializers.ModelSerializer):
    filiere_detail = FiliereSerializer(source='filiere', read_only=True)

    class Meta:
        model = Matiere
        fields = [
            'id',
            'filiere',
            'filiere_detail',
            'nom',
            'coefficient'
        ]


class ProfesseurSerializer(serializers.ModelSerializer):
    matieres_detail = MatiereSerializer(source='matieres',many=True, read_only=True)

    class Meta:
        model = Professeur
        fields = [
            'id',
            'nom',
            'prenom',
            'telephone',
            'email',
            'specialite',
            'matieres',
            'matieres_detail'

        ]


class EvaluationSerializer(serializers.ModelSerializer):
    etudiant = EtudiantSerializer(read_only=True)  # détail étudiant
    matiere = MatiereSerializer(read_only=True)    # détail matière

    class Meta:
        model = Evaluation
        fields = "__all__"


class EmploiDuTempsSerializer(serializers.ModelSerializer):
    classe_detail = ClasseSerializer(source='classe', read_only=True)
    matiere_detail = MatiereSerializer(source='matiere', read_only=True)
    professeur_detail = ProfesseurSerializer(source='professeur', read_only=True)
    filiere_detail = FiliereSerializer(source='filiere', read_only=True)

    class Meta:
        model = EmploiDuTemps
        fields = [
            'id',
            'jour',
            'heure_debut',
            'heure_fin',
            'classe_detail',
            'matiere_detail',
            'professeur_detail',
            'filiere_detail',
            'filiere', 'professeur', 'matiere', 'classe'
        ]


class AbsenceRetardSerializer(serializers.ModelSerializer):
    matiere_detail = MatiereSerializer(source='matiere', read_only=True)
    etudiant_detail = EtudiantSerializer(source='etudiant', read_only=True)

    class Meta:
        model = AbsenceRetard
        fields = [
            'etudiant',
            'etudiant_detail',
            'id',
            'matiere',
            'matiere_detail',
            'type',
            'heure_debut',
            'heure_fin'
        ]
