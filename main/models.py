from django.db import models
from django.contrib.auth.models import User

class ideaDetails(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    businessName=models.CharField(max_length=50)
    businessLocation=models.CharField(max_length=30)
    businessType=models.CharField(max_length=50)
    investmentAmount=models.PositiveBigIntegerField()
    contractDuration=models.PositiveIntegerField()
    numberOfPeople=models.PositiveIntegerField()
    businessDescription=models.CharField(max_length=500)