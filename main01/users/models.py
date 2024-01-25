from django.db import models



class Users(models.Model):
    name = models.CharField(max_length=128)
    id = models.AutoField(primary_key=True)
    category = models.CharField(max_length=128)
    description = models.TextField()
    price = models.IntegerField()

