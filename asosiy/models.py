from django.db import models
from django.contrib.auth.models import User


# HOLATI = [
#     ("Not started", "Not started"),
#     ("In Progress", "In Progress"),
#     ("Completed", "Completed"),
# ]
#

class Reja(models.Model):
    name = models.CharField(max_length=50)
    date = models.DateField(blank=True, null=True)
    details = models.TextField()
    status = models.CharField(max_length=20)
    egasi = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name
