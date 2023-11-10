from django.db import models

HOLATI = [
    ("Not started", "Not started"),
    ("In Progress", "In Progress"),
    ("Completed", "Completed"),
]


class Reja(models.Model):
    name = models.CharField(max_length=50)
    date = models.DateField(blank=True)
    details = models.TextField()
    status = models.CharField(max_length=20, choices=HOLATI)

    def __str__(self):
        return self.task
