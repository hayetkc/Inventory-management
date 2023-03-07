from django.urls import path
from . import views
urlpatterns = [ 
    path('search_produit/',views.rechercher_produits, name="listing"),
    path('search_typeProduit/',views.rechercher_typeProduits, name="listing"),
    path('search_client/',views.rechercher_clients, name="listing"),
    path('search_fournisseur/',views.rechercher_fournisseurs, name="listing"),
    path('produits/', views.produit_all, name='produits'),
    path('add-client', views.AjouterClinetView.as_view(), name='add-client'),
    path('add-produit', views.AjouterProduitView.as_view(), name='add-produit')
    ]