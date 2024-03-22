from django.db import models

# Create your models here.
class Citations(models.Model):
    texte = models.CharField(max_length=20000)
    auteur = models.CharField(max_length=200)
    thèmes= models.CharField(max_length=20000)

    def __str__(self):
        return f"{self.thèmes} - {self.texte} - {self.auteur}"
    
