from django.db import models

class Students(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    age = models.IntegerField()
    address = models.TextField()

    def __str__(self):
        return self.name

# Create your models here.