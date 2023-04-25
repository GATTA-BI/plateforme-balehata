from django.db import models

# Create your models here.
class Administration(models.Model):

    MATIERE=((' PROF:MATHS','PROF:MATHS'),
             ('PROF:PC', 'PROF:PC'),
             ('PROF:SVT', 'PROF:SVT'),
             ('PROF:FRAN', 'PROF:FRAN'),
             ('PROF:ANG', 'PROF:ANG'),
             ('PROF:HG', 'PROF:HG'),
             ('PROF:PHILO', 'PROF:PHILO'),
             ('PROF:ALL','PROF:ALL'),
             ('PROF:ESPA', 'PROF:ESPA'),
             ('PROF:EDHC', 'PROF:EDHC'),
             ('PROF:INFO', 'PROF:INFO'),
             ('PROF:EPS', 'PROF:EPS'),
             ('Enseign:CP1','Enseign:CP1'),
            ('Enseign:CP2', 'Enseign:CP2'),
            ('Enseign:CE1', 'Enseign:CE1'),
            ('Enseign:CE2', 'Enseign:CE2'),
            ('Enseign:CM1', 'Enseign:CM1'),
            ('Enseign:CM2', 'Enseign:CM2'),
             ('Educateur','Educateur'),
             ('Caissière', 'Caissière'),
             ('Stagiaire', 'Stagiaire'),
             ('Gardiennage', 'Gardiennage'))

    nom=models.CharField(max_length=200, null=True)
    fonction=models.CharField(max_length=200, null=True, choices=MATIERE)
    telephone=models.CharField (max_length=200, null=True)
    # date=models.DateTimeField(auto_now_add=True, null=True)
    #signature=

    def __str__(self):
        return self.nom
