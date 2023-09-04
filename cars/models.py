from django.db import models

# Create your models here.
class Cars(models.Model):
    Modele = models.CharField(max_length=50)
    Price= models.DecimalField(max_digits=10, decimal_places=2)

class User(models.Model):
    pass
