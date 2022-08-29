from django.db import models

# Create your models here.
class BusinessPermit(models.Model):
    personel_assignment = models.CharField("Personel Assignment", max_length=245, editable=True)
    stores = models.CharField("Stores", max_length=245, editable=True)
    


