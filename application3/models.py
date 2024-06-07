
from django.db import models
class reporters(models.Model):
    first_name=models.CharField(max_length=28)
    last_name=models.CharField(max_length=30)
    p1=models.CharField(max_length=40)
    p2=models.CharField(max_length=40)
    email=models.EmailField()
class article(models.Model):
    headlines=models.CharField(max_length=50)
    publice_date=models.DateField()
    reporters=models.ForeignKey(reporters,on_delete=models.CASCADE,primary_key=True)

   


# Create your models here.
