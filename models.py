from ipaddress import summarize_address_range
from django.db import models
from django.utils import timezone

# Create your models here.

class TypeProduit(models.Model):
    code_type_prdt = models.CharField(max_length=100,blank=True, null=True)
    nom_type_prdt = models.CharField(max_length=250)
    description = models.TextField()
    date_created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.code_type_prdt

class Fournisseur(models.Model):
    code_fournisseur = models.CharField(max_length=50,blank=True, null=True)
    nom_fournissuer = models.CharField(max_length=50)
    prenom_fournissuer = models.CharField(max_length=50)
    adresse_fournisseur = models.CharField(max_length=50)
    tel_fournissuer = models.CharField(max_length=20)

    def __str__(self):
        return self.code_fournisseur

class Produit(models.Model):
    code_prdt = models.CharField(max_length=250,blank=True, null=True)
    nom_prdt = models.CharField(max_length=250,blank=True, null=True)
    design_prdt = models.TextField()
    prixU = models.FloatField()
    date_created = models.DateTimeField(default=timezone.now)
    code_type = models.ForeignKey(TypeProduit, on_delete=models.CASCADE)
    fournisseur = models.ForeignKey(Fournisseur, on_delete= models.CASCADE)

    class Meta:
        verbose_name = "produit"
        verbose_name_plural = "produits"

    def __str__(self):
        return self.nom_prdt

class Document(models.Model):
    Num_doc= models.CharField(max_length = 250)
    design_doc = models.CharField(max_length = 250)
    total = models.DecimalField(max_digits=10000, decimal_places=2)
    date_doc = models.DateTimeField(default=timezone.now)
    typeDocument = models.ForeignKey(TypeProduit, on_delete= models.CASCADE)

    class Meta:
        verbose_name = "Document"
        verbose_name_plural = "Documents"

    def __str__(self):
           return str(self.magasinier.nom_magasin)

    @property
    def get_total(self):
        articles = self.article_set.all()   
        total = sum(article.get_total for article in articles)
        return total    

class TypeDocument(models.Model):
    Code_type_doc = models.CharField(max_length=250,blank=True, null=True)
    Nom_type_document = models.CharField(max_length=250)

def __str__(self):
        return str(self.Nom_type_document)

#stock etat+ sortie + entree
class Stock(models.Model):
    design_prdt = models.ForeignKey(Produit, on_delete=models.CASCADE)
    qte_stock = models.FloatField(default=0)
    design_type_prdt = models.ForeignKey(TypeProduit, on_delete=models.CASCADE)
    type = models.CharField(max_length=2,choices=(('1','Entrée-Stock'),('2','Sortie-Stock'),('3','En Stock')), default = 1)
    date_created = models.DateTimeField(default=timezone.now)
    date_updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return str(self.design_prdt)

    def total_stock(self):
        stocks = Stock.objects.filter(design_prdt = self)
        stockEntree = 0
        stockSortie = 0
        for stock in stocks:
            if stock.type == '1':
                stockEntree = int(stockEntree) + int(stock.qte_stock)
            else:
                stockSortie = int(stockSortie) + int(stock.qte_stock)
        Stock.qte_stock =+ stockEntree - stockSortie
        return Stock.qte_stock
# vente


class Document_Produit(models.Model):
    document = models.ForeignKey(Document, on_delete=models.CASCADE)
    produit = models.ForeignKey(Produit, on_delete=models.CASCADE)
    stock = models.ForeignKey(Stock, on_delete=models.CASCADE, blank= True, null= True)
    price = models.FloatField(default=0)
    qte_stock = models.FloatField(default=0)

    def __str__(self):
        return str(self.document.Num_doc)

class Client(models.Model):
    Code_cl = models.CharField(max_length=100,blank=True, null=True)
    nom_cl = models.CharField(max_length=100,blank=True, null=True)
    prenom_cl = models.CharField(max_length=100)
    adresse_cl = models.CharField(max_length=100)
    tel_cl = models.CharField(max_length=100)

    def __str__(self):
        return str(self.Code_cl)


class Article (models.Model):
    document = models.ForeignKey(Document, on_delete=models.CASCADE)
    produit = models.ForeignKey(Produit, on_delete=models.CASCADE)
    qte_com = models.IntegerField(default=1)
    commande = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Article'
        verbose_name_plural = 'Articles'

    @property
    def get_total(self):
        total = self.qte_com * self.produit.prix_unite_ht   
        return total 

    def __str__(self):
        return f"{self.produit.nom_prdt} ({self.qte_com})"

class BonCommande (models.Model):
    Num_com = models.CharField(max_length=100,blank=True, null=True)
    date_com = models.DateTimeField(blank=True, null=True)
    fournisseur = models.ForeignKey(Fournisseur,on_delete=models.CASCADE)
    articles = models.ManyToManyField(Article)
    conmmande = models.BooleanField(default=False)

    def __str(self):
        return self.fournisseur.nom_fournissuer

class Client(models.Model):
    Code_cl = models.CharField(max_length=100,blank=True, null=True)
    nom_cl = models.CharField(max_length=100,blank=True, null=True)
    prenom_cl = models.CharField(max_length=100)
    adresse_cl = models.CharField(max_length=100)
    tel_cl = models.CharField(max_length=100)
    credit_cl=models.FloatField(default=0)

    def __str__(self):
        return str(self.Code_cl)


class Vente(models.Model):
    Num_vente = models.CharField(max_length = 250)
    Num_client = models.ForeignKey(Client, on_delete=models.CASCADE)
    total = models.FloatField(default= 0)
    date_created = models.DateTimeField(default=timezone.now)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.Num_vente


class Produit_Vente(models.Model):
    Num_vente = models.ForeignKey(Vente, on_delete=models.CASCADE)
    produits = models.ManyToManyField(Produit,related_name="Produits")
    stock = models.ForeignKey(Stock, on_delete=models.CASCADE, blank= True, null= True)
    prix_vente = models.FloatField(default=0)
    qte_vente = models.FloatField(default=0)

    def __str__(self):
        return str(self.Num_vente)

