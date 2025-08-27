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
    menu = load_menu()
    return render(request,'parent.html',
                  {
                      'menu':menu,
                      'show_sidebar': True,
                  })

def etudiant(request):
    menu = load_menu()
    return render(request,'etudiant.html',
                  {
                      'menu':menu,
                      'show_sidebar': True,
                  })

def absence(request):
    menu = load_menu()
    return render(request,'absence.html',
                  {
                      'menu':menu,
                      'show_sidebar': True,
                  })

def classe(request):
    menu = load_menu()
    return render(request,'classe.html',
                  {
                      'menu':menu,
                      'show_sidebar': True,
                  })

def emploi(request):
    menu = load_menu()
    return render(request,'emploi.html',
                  {
                      'menu':menu,
                      'show_sidebar': True,
                  })

def matiere(request):
    menu = load_menu()
    return render(request,'matiere.html',
                  {
                      'menu':menu,
                      'show_sidebar': True,
                  })

def professeur(request):
    menu = load_menu()
    return render(request,'professeur.html',
                  {
                      'menu':menu,
                      'show_sidebar': True,
                  })