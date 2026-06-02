from django.db import models

class login(models.Model):
    name=models.CharField(max_length=100)
    password=models.CharField(max_length=20)
    emailid=models.TextField(blank=True,null=True)

    def __str__(self):
       return self.name
# Create your models here.
