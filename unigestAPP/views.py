from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from requests.exceptions import HTTPError
from django.http import HttpResponse
from django.conf import settings
import json
import os

from .models import EmploiDuTemps, Filiere
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

    for item in hori:
        try:
            count = len(APIService.get_list(item["url"]))
        except Exception as e:
            count = 0
        item["num"] = count

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
    auth_token = request.session.get('auth_token')

    if request.method == "POST":
        data = {
            "nom": request.POST.get("nom"),
            "prenom": request.POST.get("prenom"),
            "email": request.POST.get("email"),
            "telephone": request.POST.get("telephone"),
            "motDePasse": request.POST.get("motDePasse"),
        }

        response = APIService.create("parents", data, auth_token)

        if "error" not in response:
            messages.success(request, "Parent ajouté avec succès")
        else:
            messages.error(request, f"Erreur lors de l’ajout  {response['error']}")

        # Rediriger vers la même page après le POST
        return redirect("parents")  # utilise le name de ton url dans urls.py

    parent_list = APIService.get_list("parents")

    return render(
        request,
        "parents.html",
        {
            "menu": menu,
            "parent_liste": parent_list,
            "show_sidebar": True,
        }
    )

def edit_parent(request, pk):
    menu = load_menu()
    auth_token = request.session.get('auth_token')
    # Charger les données existantes
    parent_data = APIService.get_detail("parents", pk,auth_token)

    if request.method == "POST":

        data = {
            "nom": request.POST.get("nom"),
            "prenom": request.POST.get("prenom"),
            "email": request.POST.get("email"),
            "telephone": request.POST.get("telephone"),
            "motDePasse": request.POST.get("motDePasse"),
        }

        response = APIService.update("parents", pk, data,auth_token)

        if "error" not in response:
            messages.success(request, "Ajouté avec succès")
        else:
            messages.error(request, f"Erreur lors de l’ajout  {response['error']}")

        # Rediriger vers la même page après le POST
        return redirect("parents")

    return render(
        request,
        "parents.html",
        {"menu": menu, "parent": parent_data, "show_sidebar": True},
    )

def delete_parent(request, pk):
    if request.method == "POST":
        token = request.session.get("auth_token")
        try:
            result = APIService.delete("parents", pk, token=token)
            if result:
                messages.success(request, "parent supprimé avec succès")
        except request.exceptions.HTTPError as e:
            messages.error(request, f"Erreur : {e}")
    return redirect("parents")

def etudiant(request):
    menu = load_menu()
    etudiant_list = APIService.get_list("etudiants")
    parent_list = APIService.get_list("parents")
    classe_list = APIService.get_list("classes")

    auth_token = request.session.get('auth_token')

    if request.method == "POST":
        data = {
            "parent": request.POST.get("parent"),
            "classe": request.POST.get("classe"),
            "nom": request.POST.get("nom"),
            "prenom": request.POST.get("prenom"),
            "motdepasse": request.POST.get("prenom"),
            "sexe": request.POST.get("sexe"),
            "matricule": request.POST.get("matricule"),
            "dateNaissance": request.POST.get("dateNaissance"),
            "adresse": request.POST.get("adresse"),
            "telephone": request.POST.get("telephone"),
            "email": request.POST.get("email")
        }

        response = APIService.create("etudiants", data, auth_token)
        print("DEBUG CREATE ETUDIANT:", response)

        if "error" not in response:
            messages.success(request, "etudiant ajouté avec succès")
        else:
            messages.error(request, f"Erreur lors de l’ajout  {response['error']}")
            print(f"Erreur lors de l’ajout  {response['error']}")

        # Rediriger vers la même page après le POST
        return redirect("etudiants")

    return render(request, "etudiants.html", {
            "menu": menu,
            "etudiant_liste": etudiant_list,
        "parent_list":parent_list,
        "classe_list":classe_list,
            "show_sidebar": True,
        })

def edit_etudiant(request,pk):
    menu = load_menu()
    etudiant_list = APIService.get_list("etudiants")
    parent_list = APIService.get_list("parents")
    classe_list = APIService.get_list("classes")

    auth_token = request.session.get('auth_token')

    if request.method == "POST":
        data = {
            "parent": request.POST.get("parent"),
            "classe": request.POST.get("classe"),
            "nom": request.POST.get("nom"),
            "prenom": request.POST.get("prenom"),
            "motdepasse": request.POST.get("prenom"),
            "sexe": request.POST.get("sexe"),
            "matricule": request.POST.get("matricule"),
            "dateNaissance": request.POST.get("dateNaissance"),
            "adresse": request.POST.get("adresse"),
            "telephone": request.POST.get("telephone"),
            "email": request.POST.get("email")
        }

        response = APIService.update("etudiants",pk, data, auth_token)

        if "error" not in response:
            messages.success(request, " avec succès")
        else:
            messages.error(request, f"Erreur lors de l’ajout  {response['error']}")

        # Rediriger vers la même page après le POST
        return redirect("etudiants")

    return render(request, "etudiants.html", {
            "menu": menu,
            "etudiant_list": etudiant_list,
        "parent_list":parent_list,
        "classe_list":classe_list,
            "show_sidebar": True,
        })

def delete_etudiant(request, pk):
    if request.method == "POST":
        token = request.session.get("auth_token")
        try:
            result = APIService.delete("etudiants", pk, token=token)
            if result:
                messages.success(request, "etudiants supprimé avec succès")
        except request.exceptions.HTTPError as e:
            messages.error(request, f"Erreur : {e}")
    return redirect("etudiants")

def absence(request):
    menu = load_menu()
    absence_list = APIService.get_list("absences-retards")
    etudiant_list = APIService.get_list("etudiants")
    matiere_list = APIService.get_list("matieres")

    auth_token = request.session.get("auth_token")

    if request.method == "POST":
        data = {
            "etudiant": request.POST.get("etudiant"),
            "matiere": request.POST.get("matiere"),
            "type": request.POST.get("type"),
            "heure_debut": request.POST.get("heure_debut"),
            "heure_fin": request.POST.get("heure_fin")
        }

        response = APIService.create("absences-retards", data, auth_token)

        if "error" not in response:
            messages.success(request, "Ajouté avec succès")
            print(response)
        else:
            messages.error(request, f"Erreur lors de l’ajout  {response['error']}")
            print(response['error'])

            # Rediriger vers la même page après le POST
        return redirect("absences-retards")

    return render(request,'absences-retards.html',
                  {
                      'menu':menu,
                      'matiere_list':matiere_list,
                      'etudiant_list':etudiant_list,
                      'absence_liste': absence_list,
                      'show_sidebar': True,
                  })


def edit_absence(request,pk):
    menu = load_menu()
    absence_list = APIService.get_list("absences-retards")
    etudiants_list = APIService.get_list("etudiants")
    matiere_list = APIService.get_list("matieres")

    auth_token = request.session.get("auth_token")

    if request.method == "POST":
        data = {
            "etudiant": request.POST.get("etudiant"),
            "matiere": request.POST.get("matiere"),
            "type": request.POST.get("type"),
            "heure_debut": request.POST.get("heure_debut"),
            "heure_fin": request.POST.get("heure_fin")
        }

        response = APIService.update("absences-retards",pk, data, auth_token)

        if "error" not in response:
            messages.success(request, "avec succès")
        else:
            messages.error(request, f"Erreur lors de l’ajout  {response['error']}")

            # Rediriger vers la même page après le POST
        return redirect("absences-retards")

    return render(request, 'absences-retards.html',
                  {
                      'menu': menu,
                      'matiere_list': matiere_list,
                      'etudiants_list': etudiants_list,
                      'absence_liste': absence_list,
                      'show_sidebar': True,
                  })

def delete_absence(request, pk):
    if request.method == "POST":
        token = request.session.get("auth_token")
        try:
            result = APIService.delete("absences-retards", pk, token=token)
            if result:
                messages.success(request, "absences-retards supprimé avec succès")
        except request.exceptions.HTTPError as e:
            messages.error(request, f"Erreur : {e}")
    return redirect("absences-retards")

def classe(request):
    auth_token = request.session.get('auth_token')
    classe_list = APIService.get_list("classes")
    filiere_list = APIService.get_list("filieres")
    menu = load_menu()

    if request.method == "POST":
        data = {
            "nom": request.POST.get("nom"),
            "description": request.POST.get("description"),
            "filiere": request.POST.get("filiere"),
            "annee_universitaire": request.POST.get("annee_universitaire"),
        }

        response = APIService.create("classes", data, auth_token)

        if "error" not in response:
            messages.success(request, "ajouté avec succès")
        else:
            messages.error(request, f"Erreur lors de l’ajout  {response['error']}")

        # Rediriger vers la même page après le POST
        return redirect("classes")

    return render(request,'classes.html',
                  {
                      'menu':menu,
                      'filiere_list':filiere_list,
                      'classe_liste': classe_list,
                      'show_sidebar': True,
                  })

def edit_classe(request, pk):
    auth_token = request.session.get('auth_token')
    menu = load_menu()

    # Récupérer la classe à modifier
    classe_list = APIService.get_list("classes")
    filiere_list = APIService.get_list("filieres")

    if request.method == "POST":
        data = {
            "nom": request.POST.get("nom"),
            "description": request.POST.get("description"),
            "filiere": request.POST.get("filiere"),  # ⚠️ important
            "annee_universitaire": request.POST.get("annee_universitaire"),
        }

        response = APIService.update("classes", pk, data, auth_token)

        if "error" not in response:
            messages.success(request, "Classe modifiée avec succès")
            return redirect("classes")
        else:
            messages.error(request, f"Erreur lors de la modification : {response['error']}")

    return render(request, "classes.html", {
        "menu": menu,
        "classe_liste": classe_list,
        "filiere_list": filiere_list,
        "show_sidebar": True,
    })

def delete_classe(request, pk):
    if request.method == "POST":
        token = request.session.get("auth_token")
        try:
            result = APIService.delete("classes", pk, token=token)
            if result:
                messages.success(request, "classes supprimé avec succès")
        except request.exceptions.HTTPError as e:
            messages.error(request, f"Erreur : {e}")
    return redirect("classes")

def emplois(request):
    menu = load_menu()
    filieres_list = APIService.get_list("filieres")
    print("AWA",filieres_list)
    return render(request,'emplois.html',
                  {
                      'menu':menu,
                      'filieres_list':filieres_list,
                      'show_sidebar': True,
                  })

def emploi(request,pk):
    menu = load_menu()
    fil = get_object_or_404(Filiere, pk=pk)
    filieres_list = APIService.get_list("filieres")
    matieres_list = APIService.get_list("matieres")
    classes_list = APIService.get_list("classes")
    professeurs_list = APIService.get_list("professeurs")
    auth_token = request.session.get('auth_token')

    if request.method == "POST":
        data = {
            "filiere": fil.id,
            "professeur": request.POST.get("professeur"),
            "matiere": request.POST.get("matiere"),
            "classe": request.POST.get("classe"),
            "jour": request.POST.get("jour"),
            "heure_debut": request.POST.get("heure_debut"),
            "heure_fin": request.POST.get("heure_fin"),
        }

        response = APIService.create("emploi", data, auth_token)

        if response and "error" not in response:
            messages.success(request, "Ajouté avec succès")
        elif response and "error" in response:
            messages.error(request, f"Erreur lors de l’ajout : {response['error']}")
        else:
            messages.error(request, "Erreur : aucune réponse reçue du serveur.")

        # Rediriger vers la même page après le POST
        return redirect("emploi",pk = fil.id)

    emp = EmploiDuTemps.objects.filter(filiere=fil.id)

    return render(request,'emploi.html',
                  {
                      'menu':menu,
                      'fil':fil,
                      'emp':emp,
                      'filieres_list':filieres_list,
                      'matieres_list':matieres_list,
                      'classes_list':classes_list,
                      'professeurs_list':professeurs_list,
                      'show_sidebar': True,
                  })

def edit_emploi(request, emploi_id):
    menu = load_menu()
    emps = get_object_or_404(EmploiDuTemps, pk=emploi_id)
    fil = emps.filiere

    filieres_list = APIService.get_list("filieres")
    matieres_list = APIService.get_list("matieres")
    classes_list = APIService.get_list("classes")
    professeurs_list = APIService.get_list("professeurs")
    auth_token = request.session.get('auth_token')

    if request.method == "POST":
        data = {

            "filiere": fil.id,
            "professeur": request.POST.get("professeur"),
            "matiere": request.POST.get("matiere"),
            "classe": request.POST.get("classe"),
            "jour": request.POST.get("jour"),
            "heure_debut": request.POST.get("heure_debut"),
            "heure_fin": request.POST.get("heure_fin"),
        }

        response = APIService.update("emploi",emploi_id, data, auth_token)

        if response and "error" not in response:
            messages.success(request, "Modifié avec succès")
        elif response and "error" in response:
            messages.error(request, f"Erreur lors de la modification : {response['error']}")
        else:
            messages.error(request, "Erreur : aucune réponse reçue du serveur.")

        return redirect("emploi", pk=fil.id)

    emp = EmploiDuTemps.objects.filter(filiere=fil.id)

    return render(request, 'emploi_edit.html', {
        'menu': menu,
        'fil': fil,
        'emp': emp,
        'filieres_list': filieres_list,
        'matieres_list': matieres_list,
        'classes_list': classes_list,
        'professeurs_list': professeurs_list,
        'show_sidebar': True,
    })


def delete_emploi(request, pk):
    if request.method == "POST":
        token = request.session.get("auth_token")
        try:
            # Récupérer l'emploi pour avoir la filière
            emploi_obj = EmploiDuTemps.objects.get(pk=pk)
            filiere_id = emploi_obj.filiere.id

            result = APIService.delete("emploi", pk, token=token)
            if result:
                messages.success(request, "Emploi supprimé avec succès")
        except EmploiDuTemps.DoesNotExist:
            messages.error(request, "Emploi introuvable")
        except request.exceptions.HTTPError as e:
            messages.error(request, f"Erreur : {e}")

    # Rediriger vers la page de la filière
    return redirect("emploi", pk=filiere_id)



def matiere(request):
    matiere_list = APIService.get_list("matieres")
    menu = load_menu()

    filiere_list = APIService.get_list("filieres")

    auth_token = request.session.get("auth_token")

    if request.method == "POST":
        data = {
            "filiere": request.POST.get("filiere"),
            "nom": request.POST.get("nom"),
            "coefficient": request.POST.get("coefficient")
        }

        response = APIService.create("matieres", data, auth_token)

        if "error" not in response:
            messages.success(request, "Ajouté avec succès")
        else:
            messages.error(request, f"Erreur lors de l’ajout  {response['error']}")

            # Rediriger vers la même page après le POST
        return redirect("matieres")

    return render(request,'matieres.html',
                  {
                      'menu':menu,
                     'matiere_liste': matiere_list,
                      'filiere_list':filiere_list,
                      'show_sidebar': True,
                  })


def edit_matiere(request,pk):
    matiere_list = APIService.get_list("matieres")
    menu = load_menu()

    filiere_list = APIService.get_list("filieres")

    auth_token = request.session.get("auth_token")

    if request.method == "POST":
        data = {
            "nom": request.POST.get("nom"),
            "filiere": request.POST.get("filiere"),
            "coefficient": request.POST.get("coefficient")
        }

        response = APIService.update("matieres",pk, data, auth_token)

        if "error" not in response:
            messages.success(request, "modifier avec succès")
        else:
            messages.error(request, f"Erreur lors de l’ajout  {response['error']}")

            # Rediriger vers la même page après le POST
        return redirect("matieres")

    return render(request, 'matieres.html',
                  {
                      'menu': menu,
                      'matiere_liste': matiere_list,
                      'filiere_list': filiere_list,
                      'show_sidebar': True,
                  })

def delete_matiere(request, pk):
    if request.method == "POST":
        token = request.session.get("auth_token")
        try:
            result = APIService.delete("matieres", pk, token=token)
            if result:
                messages.success(request, "matieres supprimé avec succès")
        except request.exceptions.HTTPError as e:
            messages.error(request, f"Erreur : {e}")
    return redirect("matieres")

def professeur(request):
    menu = load_menu()
    professeurs_list = APIService.get_list("professeurs")
    auth_token = request.session.get("auth_token")
    matiere_list = APIService.get_list("matieres")

    if request.method == "POST":
        data = {
            "nom": request.POST.get("nom"),
            "prenom": request.POST.get("prenom"),
            "telephone": request.POST.get("telephone"),
            "email": request.POST.get("email"),
            "specialite": request.POST.get("specialite"),
            "matieres": request.POST.getlist("matieres")
        }

        prof = APIService.create("professeurs", data, auth_token)


        if "error" not in prof:
            messages.success(request, "Ajouté avec succès")
        else:
            messages.error(request, f"Erreur lors de l’ajout  {prof['error']}")
            print(request, f"Erreur lors de l’ajout  {prof['error']}")

            # Rediriger vers la même page après le POST
        return redirect("professeurs")

    return render(request,'professeurs.html',
                  {
                      'menu':menu,
                      'matiere_list':matiere_list,
                      'professeurs_liste': professeurs_list,
                      'show_sidebar': True,
                  })

def edit_professeur(request, pk):
    menu = load_menu()
    professeurs_list = APIService.get_list("professeurs")
    auth_token = request.session.get("auth_token")
    matiere_list = APIService.get_list("matieres")

    if request.method == "POST":
        data = {
            "nom": request.POST.get("nom"),
            "prenom": request.POST.get("prenom"),
            "telephone": request.POST.get("telephone"),
            "email": request.POST.get("email"),
            "specialite": request.POST.get("specialite"),
            "matieres": request.POST.getlist("matieres")
        }

        prof = APIService.update("professeurs",pk, data, auth_token)


        if "error" not in prof:
            messages.success(request, "Modifier avec succès")
        else:
            messages.error(request, f"Erreur lors de l’ajout  {prof['error']}")
            print(request, f"Erreur lors de l’ajout  {prof['error']}")

            # Rediriger vers la même page après le POST
        return redirect("professeurs")

    return render(request,'professeurs.html',
                  {
                      'menu':menu,
                      'matiere_list':matiere_list,
                      'professeurs_liste': professeurs_list,
                      'show_sidebar': True,
                  })

def delete_professeur(request, pk):
    if request.method == "POST":
        token = request.session.get("auth_token")
        try:
            result = APIService.delete("professeurs", pk, token=token)
            if result:
                messages.success(request, "professeurs supprimé avec succès")
        except request.exceptions.HTTPError as e:
            messages.error(request, f"Erreur : {e}")
    return redirect("professeurs")


def filiere(request):
    menu = load_menu()
    filiere_list = APIService.get_list("filieres")

    auth_token = request.session.get("auth_token")

    if request.method == "POST":
        data = {
            "nomfiliere": request.POST.get("nomfiliere"),
            "groupe": request.POST.get("groupe")
        }

        response = APIService.create("filieres", data, auth_token)

        if "error" not in response:
            messages.success(request, "Ajouté avec succès")
        else:
            messages.error(request, f"Erreur lors de l’ajout  {response['error']}")

            # Rediriger vers la même page après le POST
        return redirect("filieres")

    return render(request,'filieres.html',
                  {
                      'menu':menu,
                      'filiere_liste': filiere_list,
                      'show_sidebar': True,
                  })

def edit_filiere(request, pk):
    menu = load_menu()
    auth_token = request.session.get("auth_token")

    # Charger la filière existante
    filiere_data = APIService.get_detail("filieres", pk)

    if request.method == "POST":
        data = {
            "nomfiliere": request.POST.get("nomfiliere"),
            "groupe": request.POST.get("groupe"),
        }

        response = APIService.update("filieres", pk, data, auth_token)

        if "error" not in response:
            messages.success(request, "Modifier avec succès")
        else:
            messages.error(request, f"Erreur lors de l’ajout  {response['error']}")

            # Rediriger vers la même page après le POST
        return redirect("filieres")

    return render(
        request,
        "filieres.html",
        {"menu": menu, "filiere": filiere_data, "show_sidebar": True}
    )

def delete_filiere(request, pk):
    if request.method == "POST":
        token = request.session.get("auth_token")
        try:
            result = APIService.delete("filieres", pk, token=token)
            if result:
                messages.success(request, "filieres supprimé avec succès")
        except request.exceptions.HTTPError as e:
            messages.error(request, f"Erreur : {e}")
    return redirect("filieres")

def evaluation(request):
    menu = load_menu()


    auth_token = request.session.get("auth_token")

    return render(request,'evaluation.html',
                  {
                      'menu':menu,
                      'show_sidebar': True,
                  })