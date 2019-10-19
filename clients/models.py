from django.db import models

# Create your models here.
class Client(models.Model):
    patient_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    other_names = models.CharField(max_length=250)
    filled = models.CharField(max_length=250)
    id_number = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=15)
    race = models.CharField(max_length=250)
    gender = models.CharField(max_length=250)
    dob = models.DateField(max_length=10)
    occupation = models.CharField(max_length=250)
    income = models.CharField(max_length=250)
    education = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.first_name