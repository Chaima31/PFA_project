
# models.py
from django.db import models
from django import forms


class bondedecommandee(models.Model):
    # Changed field names and types based on your table changes

    Code_Article_magasin = models.IntegerField()
    Code_Barre = models.CharField(max_length=17)
    Designation_article = models.CharField(max_length=40)
    UV = models.CharField(max_length=5)

    def __str__(self):
        return str(self.Code_Article)
class bondedecommandeeee(models.Model):
    # Changed field names and types based on your table changes

    Code_Article_magasin = models.IntegerField()
    Code_Barre = models.CharField(max_length=17)
    Designation_article = models.CharField(max_length=40)
    UV = models.CharField(max_length=5)
    Colisage=models.IntegerField()

    def __str__(self):
        return str(self.Code_Article)

class bondedecommandeee(models.Model):
        # Changed field names and types based on your table changes

        Code_Article_magasin = models.IntegerField()
        Code_Barre = models.CharField(max_length=17)
        Designation_article = models.CharField(max_length=40)
        UV = models.CharField(max_length=5)
        Colisage = models.IntegerField()

        def __str__(self):
            return str(self.Code_Article)


from django.db import models

class Report(models.Model):

    excel_filename = models.CharField(max_length=255)

    excel_content = models.BinaryField()  # Stocker le contenu Excel
    date = models.DateField()






class Client(models.Model):

    Code_Client = models.IntegerField()
    Nom_Client = models.CharField(max_length=36)
    Groupe_Vendeur = models.IntegerField()
    Designation_Vendeur = models.CharField(max_length=18)
    Organis_commerciale = models.CharField(max_length=4)
    Canal_distribution = models.CharField(max_length=2)
    Secteur_activite = models.CharField(max_length=2)
    Conditions_paiement = models.CharField(max_length=3)
    Agence_commerciale = models.CharField(max_length=4)
    DIVISON = models.CharField(max_length=255)  # Replace 255 with the appropriate max length

    def __str__(self):
        return self.Nom_Client



class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = '__all__'  # Utilisez '__all__' pour inclure tous les champs du modèle

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['Code_Client'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Code Client',
            # Ajoutez d'autres attributs HTML ou styles CSS personnalisés ici
        })

        self.fields['Nom_Client'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Nom Client',
            # Ajoutez d'autres attributs HTML ou styles CSS personnalisés ici
        })

        self.fields['Groupe_Vendeur'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Groupe Vendeur',
            # Ajoutez d'autres attributs HTML ou styles CSS personnalisés ici
        })
        self.fields['Designation_Vendeur'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Designation_Vendeur',
            # Ajoutez d'autres attributs HTML ou styles CSS personnalisés ici
        })
        self.fields['Organis_commerciale'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Organis_commerciale',
            # Ajoutez d'autres attributs HTML ou styles CSS personnalisés ici
        })
        self.fields['Canal_distribution'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Canal_distribution',
            # Ajoutez d'autres attributs HTML ou styles CSS personnalisés ici
        })
        self.fields['Secteur_activite'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Secteur_activite',
            # Ajoutez d'autres attributs HTML ou styles CSS personnalisés ici
        })
        self.fields['Conditions_paiement'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Conditions_paiement',
            # Ajoutez d'autres attributs HTML ou styles CSS personnalisés ici
        })
        self.fields['Agence_commerciale'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Agence_commerciale',
            # Ajoutez d'autres attributs HTML ou styles CSS personnalisés ici
        })
        self.fields['DIVISON'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'DIVISON',
            # Ajoutez d'autres attributs HTML ou styles CSS personnalisés ici
        })


        # Ajoutez les autres champs ici en utilisant le même modèle




class bondedecommandeForm(forms.ModelForm):
    class Meta:
        model = bondedecommandeeee
        fields = '__all__'  # Utilisez '__all__' pour inclure tous les champs du modèle unique=True,

from django.db import models

class User(models.Model):
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)

    def __str__(self):
        return self.email
