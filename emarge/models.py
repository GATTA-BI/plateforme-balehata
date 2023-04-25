from django.db import models

# Create your models here.
class Emarge(models.Model):

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
             ('EPS', 'EPS'),
             ('PRIMAIRE', 'PRIMAIRE'),
             ('Educateur','Educateur'),
             ('Caissière', 'Caissière'),
             ('Stagiaire', 'Stagiaire'),
             ('Gardiennage', 'Gardiennage'))
    
    HORAIRE=(('OK','OK'),
            ('Absent','Absent'),
            ('2heures','2heures'),
            ('3heures', '3heures'),
            ('4heures', '4heures'),
            ('5heures', '5heures'),
            ('6heures', '6heures'),
            ('7heures', '7heures'),
            ('8heures', '8heures'),
            ('9heures','9heures'),
            ('10heures', '10heures'))

    nom=models.CharField(max_length=200, null=True)
    fonction=models.CharField(max_length=200, null=True, choices=MATIERE)
    emargement=models.DateTimeField(auto_now_add=True, null=True)
    nombre_d_heures=models.CharField(max_length=12, null=True, choices=HORAIRE)


    def __str__(self):
        return self.nom
