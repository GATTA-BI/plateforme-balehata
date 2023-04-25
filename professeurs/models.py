from django.db import models

# Create your models here.
class Professeur(models.Model):

    MATIERE=(('MATHS','MATHS'),
             ('PC', 'PC'),
             ('SVT', 'SVT'),
             ('FRAN', 'FRAN'),
             ('ANG', 'ANG'),
             ('HG', 'HG'),
             ('PHILO', 'PHILO'),
             ('ALL','ALL'),
             ('ESPA', 'ESPA'),
             ('EDHC', 'EDHC'),
             ('INFO', 'INFO'),
             ('EPS', 'EPS'))

    nom=models.CharField(max_length=200, null=True)
    matiere=models.CharField(max_length=200, null=True, choices=MATIERE)
    annee=models.CharField(max_length=200, null=True)
    telephone=models.CharField (max_length=200, null=True)
    #date_creation=models.DateTimeField(auto_now_add=True, null=True)
    

    def __str__(self):
        return self.nom
