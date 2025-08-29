import self
from django.http.multipartparser import MultiPartParser
from djoser import serializers
from rest_framework import generics
from django.contrib.auth.models import Group, User
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.permissions import IsAuthenticated
from .models import Parent, Classe, Matiere, Etudiant, Evaluation, Professeur, EmploiDuTemps, AbsenceRetard, Filiere
from .serializer import ProfesseurSerializer,ClasseSerializer,ParentSerializer,EtudiantSerializer,MatiereSerializer,EvaluationSerializer,FiliereSerializer,AbsenceRetardSerializer,EmploiDuTempsSerializer
from rest_framework import viewsets
from rest_framework import status
from django.shortcuts import render
from rest_framework.response import Response
from django.shortcuts import  get_object_or_404

class ParentView(generics.ListCreateAPIView):
    queryset = Parent.objects.all().order_by('id')
    serializer_class = ParentSerializer
    def get_permissions(self):
        permission_classes = []
        if self.request.method != 'GET':
            permission_classes = [IsAuthenticated]

        return [permission() for permission in permission_classes]


class SingleParentView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Parent.objects.all()
    serializer_class = ParentSerializer
    def get_permissions(self):
        permission_classes = []
        if self.request.method not in ['GET']:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]

class ClasseView(generics.ListCreateAPIView):
    queryset = Classe.objects.all().order_by('id')
    serializer_class = ClasseSerializer
    def get_permissions(self):
        permission_classes = []
        if self.request.method != 'GET':
            permission_classes = [IsAuthenticated]

        return [permission() for permission in permission_classes]

class SingleClasseView(generics.RetrieveUpdateDestroyAPIView):
        queryset = Classe.objects.all()
        serializer_class = ClasseSerializer
        def get_permissions(self):
            permission_classes = []
            if self.request.method not in ['GET']:
                permission_classes = [IsAuthenticated]
            return [permission() for permission in permission_classes]

class MatiereView(generics.ListCreateAPIView):
                queryset = Matiere.objects.all().order_by('id')
                serializer_class = ParentSerializer
                def get_permissions(self):
                    permission_classes = []
                    if self.request.method != 'GET':
                       permission_classes = [IsAuthenticated]
                    return [permission() for permission in permission_classes]

class SingleMatiereView(generics.RetrieveUpdateDestroyAPIView):
              queryset = Matiere.objects.all()
              serializer_class = MatiereSerializer
              def get_permissions(self):
                  permission_classes = []
                  if self.request.method not in ['GET']:
                    permission_classes = [IsAuthenticated]
                  return [permission() for permission in permission_classes]


class EtudiantView(generics.ListCreateAPIView):
              queryset = Etudiant.objects.all().order_by('id')
              serializer_class = EtudiantSerializer
              def get_permissions(self):
                   permission_classes = []
                   if self.request.method != 'GET':
                     permission_classes = [IsAuthenticated]
                   return [permission() for permission in permission_classes]


class SingleEtudiantView(generics.RetrieveUpdateDestroyAPIView):
            queryset = Etudiant.objects.all()
            serializer_class = MatiereSerializer
            def get_permissions(self):
                permission_classes = []
                if self.request.method not in ['GET']:
                 permission_classes = [IsAuthenticated]
                return [permission() for permission in permission_classes]


class EvaluationView(generics.ListCreateAPIView):
                 queryset = Evaluation.objects.all().order_by('id')
                 serializer_class = EvaluationSerializer
                 def get_permissions(self):
                     permission_classes = []
                     if self.request.method != 'GET':
                       permission_classes = [IsAuthenticated]
                     return [permission() for permission in permission_classes]


class SingleEvaluationiew(generics.RetrieveUpdateDestroyAPIView):
               queryset = Evaluation.objects.all()
               serializer_class = EvaluationSerializer
               def get_permissions(self):
                 permission_classes = []
                 if self.request.method not in ['GET']:
                       permission_classes = [IsAuthenticated]
                 return [permission() for permission in permission_classes]


class ProfesseurView(generics.ListCreateAPIView):
            queryset = Professeur.objects.all().order_by('id')
            serializer_class = ParentSerializer
            def get_permissions(self):
                permission_classes = []
                if self.request.method != 'GET':
                    permission_classes = [IsAuthenticated]

                return [permission() for permission in permission_classes]


class SingleProfessuerView(generics.RetrieveUpdateDestroyAPIView):
              queryset = Professeur.objects.all()
              serializer_class = ProfesseurSerializer
              def get_permissions(self):
                  permission_classes = []
                  if self.request.method not in ['GET']:
                       permission_classes = [IsAuthenticated]

                  return [permission() for permission in permission_classes]



class EmploiDuTempsView(generics.ListCreateAPIView):
              queryset = EmploiDuTemps.objects.all().order_by('id')
              serializer_class = EmploiDuTempsSerializer
              def get_permissions(self):
                    permission_classes = []
                    if self.request.method != 'GET':
                        permission_classes = [IsAuthenticated]

                    return [permission() for permission in permission_classes]





class SingleEmploiDuTempsView(generics.RetrieveUpdateDestroyAPIView):
          queryset = EmploiDuTemps.objects.all()
          serializer_class = EmploiDuTempsSerializer
          def get_permissions(self):
              permission_classes = []
              if self.request.method not in ['GET']:
                     permission_classes = [IsAuthenticated]
              return [permission() for permission in permission_classes]

class AbsanceRetardView(generics.ListCreateAPIView):
         queryset = AbsenceRetard.objects.all().order_by('id')
         serializer_class = AbsenceRetardSerializer
         def get_permissions(self):
              permission_classes = []
              if self.request.method != 'GET':
                  permission_classes = [IsAuthenticated]

              return [permission() for permission in permission_classes]


class SingleAbsenceRetardView(generics.RetrieveUpdateDestroyAPIView):
      queryset = AbsenceRetard.objects.all()
      serializer_class = AbsenceRetardSerializer
      def get_permissions(self):
            permission_classes = []
            if self.request.method not in ['GET']:
              permission_classes = [IsAuthenticated]
            return [permission() for permission in permission_classes]


class FiliereView(generics.ListCreateAPIView):
        queryset = Filiere.objects.all().order_by('id')
        serializer_class = ParentSerializer

        def get_permissions(self):
              permission_classes = []
              if self.request.method != 'GET':
                  permission_classes = [IsAuthenticated]

              return [permission() for permission in permission_classes]


class SingleFilieredView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Filiere.objects.all()
    serializer_class = FiliereSerializer

    def get_permissions(self):
        permission_classes = []
        if self.request.method not in ['GET']:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]

