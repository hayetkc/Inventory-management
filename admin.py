from django.contrib import admin
from .models import TypeProduit, Fournisseur, Produit, Stock, Document, TypeDocument, Client, Article, BonCommande

admin.site.register(TypeProduit)
admin.site.register(Fournisseur)
admin.site.register(Produit)
admin.site.register(Stock)
admin.site.register(Document)
admin.site.register(TypeDocument)
admin.site.register(Client)
admin.site.register(Article)
admin.site.register(BonCommande)



# Register your models here.
