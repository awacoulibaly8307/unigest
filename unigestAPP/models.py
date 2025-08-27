from django.db import models
from django.contrib.auth.models import User

class Parent(models.Model):
   
    nom = models.CharField(max_length=255)
    prenom = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    motDePasse = models.CharField()

class Etudiant(models.Model):
   
    parent = models.ForeignKey(Parent, on_delete=models.CASCADE),
    nom = models.CharField(max_length=255)
    prenom = models.CharField(max_length=255)
    motdepasse = models.TextField(max_length=255)
    DateNaissance = models. DateField()
    matricule= models.CharField(max_length=255)
    LieuNaissance = models.DateField()
    sexe = models.TextField(max_length=255)
    adresse = models.CharField(max_length=255)
    telephone = models.CharField(max_length=255)
    email = models.CharField(max_length=255)


class Classe(models.Model):
   
    etudiant = models.ForeignKey(Etudiant, on_delete=models.CASCADE),
    nom = models.CharField()


class Matiere(models.Model):
   
    NomMatiere = models.CharField(max_length=255)
    ceofficient = models.IntegerField()


class Professeur(models.Model):
   
    matiere = models.ForeignKey(Matiere, on_delete=models.CASCADE)
    nom = models.CharField(max_length=255)
    prenom = models.CharField(max_length=255)
    telephone = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    specialiste = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.specialiste}"

class Evaluation(models.Model):
    etudiant = models.ForeignKey(Etudiant, on_delete=models.CASCADE)
    matiere = models.ForeignKey(Matiere, on_delete=models.CASCADE)
    note = models.IntegerField()
    type_evaluation = models.CharField(max_length=50)
    date_evaluation = models.DateField()


class EmploiDuTemps(models.Model):
      matiere = models.ForeignKey(Matiere, on_delete=models.CASCADE)
      classe = models.ForeignKey(Classe , on_delete=models.CASCADE)
      jour = models.CharField()
      datedebut = models.DateTimeField()
      datefin = models.DateTimeField()

class AbsenceRetard(models.Model):
       
        matiere = models.ForeignKey(Matiere, on_delete=models.CASCADE)
        type = models.CharField(max_length=255)
        heureDebut = models.TimeField()
        heureFin = models.TimeField()
        DateEnregistrement =  models.DateField()
