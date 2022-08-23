from django.db import models

# Create your models here.
class Contactus(models.Model):
    name = models.CharField(max_length = 200)
    email = models.EmailField(max_length=254)
    website= models.CharField(max_length = 200)
    description = models.TextField()

class paper(models.Model):
    paperid= models.CharField(max_length = 200)
    firstname = models.CharField(max_length = 200)
    lastname = models.CharField(max_length = 200, default='SOME STRING')
    email= models.EmailField(max_length=254)
    company=models.CharField(max_length = 200)
    jobtitle=models.CharField(max_length = 200)
    country=models.CharField(max_length = 200)
    Industry=models.CharField(max_length = 200)
    Intrests= models.TextField()
class newsletter(models.Model):
    
    email= models.EmailField(max_length=254)
   
    