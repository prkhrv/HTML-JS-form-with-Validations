from django.db import models

# Create your models here.
class Profile(models.Model):
    fname = models.CharField(max_length=20)
    lname = models.CharField(max_length=20)
    email = models.EmailField(max_length=40)
    phone = models.CharField(max_length=10)
    roll = models.CharField(max_length=10,unique = True)

    def __str__(self):
        return self.fname
