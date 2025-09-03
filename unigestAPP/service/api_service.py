import requests
from django.db.models import Count
from django.db.models.functions import ExtractMonth
from datetime import date
from calendar import month_abbr
from django.db.models.functions import TruncMonth

BASE_URL = "http://127.0.0.1:8000/api/"
AUTH_URL = "http://127.0.0.1:8000/auth/"


class APIService:

    @staticmethod
    def _headers(token=None):
        """Construit les en-têtes HTTP"""
        headers = {}
        if token:
            headers["Authorization"] = f"Token {token}"
        return headers

    @staticmethod
    def get_list(resource):
        """Récupère la liste d'une ressource"""
        response = requests.get(f"{BASE_URL}{resource}")
        print(response.status_code, response.text)
        response.raise_for_status()
        return response.json()

    @staticmethod
    def get_user(token=None):
        try:
            headers = APIService._headers(token)
            response = requests.get(f"{AUTH_URL}users/", headers=headers)
            print("response : ", response.json())
            response.raise_for_status()
            return response.json()
        except Exception as e:
            return {"error": str(e)}

    @staticmethod
    def get_detail(resource, pk, token=None):
        """Récupère un élément par ID"""
        try:
            url = f"{APIService.BASE_URL}{resource}/{pk}/"
            headers = APIService._headers(token)

            response = requests.get(url, headers=headers)
            response.raise_for_status()
            return response.json()
        except Exception as e:
            return {"error": str(e)}

    @staticmethod
    def create(resource, data, token=None):
        """Ajoute un élément"""

        try:
            headers = {}

            if token:
                headers['Authorization'] = f"Token {token}"  # ou Bearer
                print("token:", token)

            response = requests.post(f"{BASE_URL}{resource}", json=data, headers=headers)
            response.raise_for_status()
            return response.json()

        except requests.exceptions.HTTPError as http_err:
            # Retourner le message d'erreur précis du backend
            try:
                print("erreur", str(response.json()))
                return {"error": response.json()}
            except:
                print("erreur", str(http_err))
                return {"error": str(http_err)}
        except Exception as err:
            print("erreur", str(err))
            return {"error": str(err)}

    @staticmethod
    def createFormData(resource, data, files=None, token=None):
        """
        Crée un nouvel élément via l'API.
        :param resource: nom de la ressource (ex: 'patients')
        :param data: dictionnaire des données à envoyer
        :param files: dictionnaire pour les fichiers (ex: {'image': open(path, 'rb')})
        """
        try:
            url = f"{BASE_URL}{resource}"
            # en-têtes d'authentification si token fourni
            headers = {}

            if token:
                headers['Authorization'] = f"Token {token}"  # ou Bearer
                print("token:", token)

            if files:
                # multipart/form-data
                response = requests.post(url, data=data, files=files, headers=headers)
            else:
                response = requests.post(url, data=data, files=files, headers=headers)

            response.raise_for_status()
            return response.json()

        except requests.exceptions.HTTPError as http_err:
            # Retourner le message d'erreur précis du backend
            try:
                print("erreur", str(response.json()))
                return {"error": response.json()}
            except:
                print("erreur", str(http_err))
                return {"error": str(http_err)}
        except Exception as err:
            print("erreur", str(err))
            return {"error": str(err)}

    @staticmethod
    def updateFormData(resource, pk, data, files=None, token=None):

        headers = APIService._headers(token)

        try:
            url = f"{BASE_URL}{resource}/{pk}"

            if files:
                # multipart/form-data
                response = requests.put(url, data=data, files=files, headers=headers)
            else:
                response = requests.put(url, data=data, files=files, headers=headers)

            response.raise_for_status()
            return response.json()

        except requests.exceptions.HTTPError as http_err:
            # Retourner le message d'erreur précis du backend
            try:
                print("erreur", str(response.json()))
                return {"error": response.json()}
            except:
                print("erreur", str(http_err))
                return {"error": str(http_err)}
        except Exception as err:
            print("erreur", str(err))
            return {"error": str(err)}

    @staticmethod
    def login(data):
        """Ajoute un élément"""
        response = requests.post(f"{AUTH_URL}token/login", json=data)
        print("login", response.status_code, response.text)
        response.raise_for_status()
        return response.json()

    @staticmethod
    def logout(token: str):
        """Déconnecte l’utilisateur"""
        headers = APIService._headers(token)
        response = requests.post(f"{AUTH_URL}token/logout/", headers=headers)
        print("logout", response.status_code, response.text)
        response.raise_for_status()

    @staticmethod
    def get_current_user(token: str):
        headers = APIService._headers(token)

        response = requests.get(f"{AUTH_URL}users/me/", headers=headers)
        response.raise_for_status()
        return response.json()

    @staticmethod
    def update(resource, pk, data, token=None):
        """Modifie un élément"""
        headers = APIService._headers(token)
        response = requests.put(f"{BASE_URL}{resource}/{pk}", json=data, headers=headers)
        response.raise_for_status()
        return response.json()

    @staticmethod
    def delete(resource, pk, token=None):
        """Supprime un élément"""
        try:
            url = f"{BASE_URL}{resource}/{pk}"  # <--- plus de /delete
            headers = APIService._headers(token)

            response = requests.delete(url, headers=headers)
            print("reponse server", response.status_code)
            response.raise_for_status()
            return True
        except Exception as e:
            return {"error": str(e)}



