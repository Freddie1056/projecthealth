from django.db import models
from django.conf import settings

# Create your models here.
class Patient(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    blood_pressure = models.CharField(max_length=10)
    blood_sugar = models.CharField(max_length=10)

    

