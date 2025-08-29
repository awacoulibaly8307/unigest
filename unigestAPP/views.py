from django.shortcuts import render, redirect
from django.contrib import messages
from requests.exceptions import HTTPError
from django.http import HttpResponse
from django.conf import settings
import json
import os
from .service.api_service import APIService
from django.db.models import Count,Avg,Sum

# Create your views here.

def load_menu():
    menu_file = os.path.join(settings.BASE_DIR,  'static', 'menu.json')
    with open(menu_file, 'r') as f:
        return json.load(f)

def load_hor():
    menu_file = os.path.join(settings.BASE_DIR,  'static', 'horizontal.json')
    with open(menu_file, 'r') as f:
        return json.load(f)

def index(request):
    menu = load_menu()
    hori = load_hor()

    return render(request,'index.html',
                  {
                      'menu':menu,
                      'hori':hori,
                      'show_sidebar': True,
                  }
    )

def home(request):
    # Si l'utilisateur est déjà connecté → redirection automatique
    # if request.user.is_authenticated:
    #     return redirect("index")
    # else:
    #    return redirect("home")

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        try:
            data = {"username": username, "password": password}
            token_data = APIService.login(data)
            request.session['auth_token'] = token_data['auth_token']

            messages.success(request, "Connexion réussie !")
            return redirect("index")

        except HTTPError:
            messages.error(request, "Identifiants incorrects.")
        except Exception as e:
            messages.error(request, f"Erreur inattendue : {str(e)}")

    return render(request, "home.html", {
        'show_sidebar': False,
        "disable_sidebar_margin": True,
        "disable_sidebar_mt": True,
    })

def parent(request):
    # Charger le menu de navigation (probablement défini dans une fonction utilitaire load_menu)
    menu = load_menu()

    # Récupérer la liste des parents via un service d'API
    # Ici, APIService.get_list("parents") appelle l'API et renvoie un tableau d'objets "parents"
    parent_list = APIService.get_list("parents")

    # Renvoyer la réponse HTTP avec le template "parent.html"
    # On transmet des variables au template sous forme de dictionnaire :
    # - 'parent_liste' : la liste des parents pour affichage dans le tableau
    return render(
        request,
        'parent.html',
        {
            'menu': menu,
            'parent_liste': parent_list,
            'show_sidebar': True,
        }
    )


def etudiant(request):
    menu = load_menu()
    etudiant_list = APIService.get_list("etudiants")
    return render(request,'etudiant.html',
                  {
                      'menu':menu,
                      'etudiant_liste':etudiant_list,
                      'show_sidebar': True,
                  })

def absence(request):
    menu = load_menu()
    absence_list = APIService.get_list("absences-retards")
    return render(request,'absence.html',
                  {
                      'menu':menu,
                      'absence_liste': absence_list,
                      'show_sidebar': True,
                  })

def classe(request):
    classe_list = APIService.get_list("classes")
    menu = load_menu()
    return render(request,'classe.html',
                  {
                      'menu':menu,
                      'classe_liste': classe_list,
                      'show_sidebar': True,
                  })

def emploi(request):
    menu = load_menu()
    emploi_list = APIService.get_list("emplois")
    return render(request,'emploi.html',
                  {
                      'menu':menu,
                      'emploi_liste': emploi_list,
                      'show_sidebar': True,
                  })

def matiere(request):
    matiere_list = APIService.get_list("matieres")
    menu = load_menu()
    return render(request,'matiere.html',
                  {
                      'menu':menu,
                     'matiere_liste': matiere_list,
                      'show_sidebar': True,
                  })

def professeur(request):
    menu = load_menu()
    professeurs_list = APIService.get_list("professeurs")
    return render(request,'professeur.html',
                  {
                      'menu':menu,
                      'professeurs_liste': professeurs_list,
                      'show_sidebar': True,
                  })



def filiere(request):
    menu = load_menu()
    filiere_list = APIService.get_list("filiere")
    return render(request,'filiere.html',
                  {
                      'menu':menu,
                      'filiere_liste': filiere_list,
                      'show_sidebar': True,
                  })