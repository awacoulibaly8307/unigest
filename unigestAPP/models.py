from django.db import models
from django.contrib.auth.models import User

class Parent(models.Model):
   
    nom = models.CharField(max_length=255)
    prenom = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    motDePasse = models.CharField()
    telephone = models.CharField(max_length=20)
    date  = models.DateField(auto_now=True)

class Filiere(models.Model):
    nomfiliere = models.CharField(max_length=255)
    groupe = models.CharField(max_length=255)
    DateEnregistrement = models.DateField(auto_now=True)

class Classe(models.Model):
    nom = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    filiere = models.ForeignKey(Filiere, on_delete=models.CASCADE)
    annee_universitaire = models.CharField(max_length=9)

    def __str__(self):
        return self.nom

class Etudiant(models.Model):
    parent = models.ForeignKey(Parent, on_delete=models.CASCADE)
    classe = models.ForeignKey(Classe, on_delete=models.CASCADE)  # relation correcte
    nom = models.CharField(max_length=255)
    prenom = models.CharField(max_length=255)
    motdepasse = models.CharField(max_length=255)
    sexe = models.CharField(max_length=10, choices=[("M", "Masculin"), ("F", "Féminin")])
    matricule = models.CharField(max_length=255, unique=True)
    dateNaissance = models.DateField()
    adresse = models.CharField(max_length=255)
    telephone = models.CharField(max_length=20)
    email = models.EmailField(unique=True)

    def __str__(self):
        return f"{self.nom} {self.prenom}"

    

class Matiere(models.Model):
    filiere = models.ForeignKey(Filiere, on_delete=models.CASCADE)
    nom = models.CharField(max_length=255)
    coefficient = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.nom}"


class Professeur(models.Model):
    nom = models.CharField(max_length=255)
    prenom = models.CharField(max_length=255)
    telephone = models.CharField(max_length=20, unique=True)
    email = models.EmailField(unique=True)
    specialite = models.CharField(max_length=255)

    # Un professeur peut enseigner plusieurs matières
    matieres = models.ManyToManyField(Matiere, related_name="professeurs")

    def __str__(self):
        return f"{self.nom} {self.prenom} - {self.specialite}"


class Evaluation(models.Model):

    etudiant = models.ForeignKey(Etudiant, on_delete=models.CASCADE)
    matiere = models.ForeignKey(Matiere, on_delete=models.CASCADE)
    note = models.DecimalField(max_digits=5, decimal_places=2)  # ex: 15.50
    type_evaluation = models.CharField(max_length=50,)
    date_evaluation = models.DateField()

    def __str__(self):
        return f"{self.date_evaluation}"


class EmploiDuTemps(models.Model):
    professeur = models.ForeignKey(Professeur, on_delete=models.CASCADE)
    matiere = models.ForeignKey(Matiere, on_delete=models.CASCADE)
    classe = models.ForeignKey(Classe, on_delete=models.CASCADE)
    jour = models.CharField(max_length=20)
    heure_debut = models.TimeField()
    heure_fin = models.TimeField()

    def __str__(self):
        return f"{self.jour}"


class AbsenceRetard(models.Model):

    etudiant = models.ForeignKey(Etudiant, on_delete=models.CASCADE)
    matiere = models.ForeignKey(Matiere, on_delete=models.CASCADE)
    type = models.CharField(max_length=20)
    heure_debut = models.TimeField()
    heure_fin = models.TimeField()
    date_enregistrement = models.DateField()

    def __str__(self):
        return f"({self.date_enregistrement})"
