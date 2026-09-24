from django.db import models
from django.contrib.auth.models import AbstractUser



# Create your models here.
class CustomUser(AbstractUser):
    class Roles(models.TextChoices):
        ADMIN="ADMIN","Administrateur"
        USER="USER","Utilisateur"
    role=models.CharField(max_length=20,choices=Roles.choices,default=Roles.USER,verbose_name="Rôle")

    def __str__(self):
        return f"{self.username} - {self.role}"
    

