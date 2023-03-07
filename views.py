from django.shortcuts import render
from .models import *
from django.views import View
from django.http import HttpResponse

from django.shortcuts import render, redirect
from django.shortcuts import render
from django.http import *
from django.views.generic import TemplateView
from django.conf import settings

class AjouterClinetView(View):
    # ajouter un nouveau client

    template_name = 'add_client.html'
    def get(self, request, *args, **kwargs):
        render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        return render(request, self.template_name)

class AjouterProduitView(View):
    # ajouter un nouveau produit

    template_name = 'add_produit.html'
    def get(self, request, *args, **kwargs):
        render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        return render(request, self.template_name)
        

def produit_all(request):
    produits = Produit.objects.all()
    context_dict = {'produits': produits}
    return render(request, "produit_all.html", context_dict)

def rechercher_produits(request):
    if request.method == "GET":
        query = request.GET.get('recherche')
        if query:
            produits = Produit.objects.filter(name_contains = query)
            return render(request, "search.html",{"produits":produits})

def rechercher_typeProduits(request):
    if request.method == "GET":
        query = request.GET.get('recherche')
        if query:
            typeProduits = TypeProduit.objects.filter(name_contains = query)
            return render(request, "search.html",{"typeProduits":typeProduits})

def rechercher_clients(request):
     if request.method == "GET":
        query = request.GET.get('recherche')
        if query:
            clients = Client.objects.filter(name_contains = query)
            return render(request, "search.html",{"clients":clients})

def rechercher_fournisseurs(request):
     if request.method == "GET":
        query = request.GET.get('recherche')
        if query:
            fournisseurs = Fournisseur.objects.filter(name_contains = query)
            return render(request, "search.html",{"fournisseurs":fournisseurs})
