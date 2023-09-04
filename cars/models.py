from django.db import models

# Create your models here.
class cars(models.Model):
    Modele = models.CharField(max_length=50)
    Price= models.CharField(max_length=50)

class User(models.Model):
    pass
