from django.db import models

# Create your models here.

class Contacts(models.Model):
    contact_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=25)
    address = models.CharField(max_length=100)
    profession = models.CharField(max_length=25)
    email = models.EmailField(max_length=254)
    tel = models.IntegerField()
   

    class Meta:
        db_table = "contacts"