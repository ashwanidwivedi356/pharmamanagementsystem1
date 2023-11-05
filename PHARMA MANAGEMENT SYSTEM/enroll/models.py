from django.db import models

# Create your models here.
class User(models.Model):
    Doctor_name = models.CharField(max_length=90)
    Specialization = models.CharField(max_length=80)
    Openning_time = models.TimeField(max_length=100)
    Closing_time = models.TimeField(max_length=100)
    Doctor_fees = models.CharField(max_length=50)






