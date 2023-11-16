from django.db import models
from django.contrib.auth.models import User, AbstractUser


class Talaba(AbstractUser):
    ism = models.CharField(max_length=30)
    kurs = models.PositiveSmallIntegerField()
    guruh = models.CharField(max_length=15)
    yonalish = models.CharField(max_length=50)
    first_name = None
    last_name = None
    last_login = None


class Reja(models.Model):
    name = models.CharField(max_length=50)
    date = models.DateField(blank=True, null=True)
    details = models.TextField()
    status = models.CharField(max_length=20)
    egasi = models.ForeignKey(Talaba, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name
