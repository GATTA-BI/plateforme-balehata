from django.db import models

# Create your models here.
class Instituteur(models.Model):
    
    CLASSE=(('CP1','CP1'),
            ('CP2', 'CP2'),
            ('CE1', 'CE1'),
            ('CE2', 'CE2'),
            ('CM1', 'CM1'),
            ('CM2', 'CM2'))

    nom=models.CharField(max_length=200, null=True)
    classe=models.CharField(max_length=200, null=True, choices=CLASSE)
    annee=models.CharField(max_length=200, null=True)
    telephone=models.CharField(max_length=200, null=True)
    #date_creation=models.DateTimeField(auto_now_add=True, null=True)
    


    def __str__(self):
        return self.nom