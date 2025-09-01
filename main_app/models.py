from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class Cat(models.Model):
    name = models.CharField(max_length=80)
    breed = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    description = models.TextField(null=True)
    is_alive = models.BooleanField(default=True)


    class Meta:
        db_table = "cats"

    def __str__(self):
        return f"{self.name}"


class Food(models.Model):
    name = models.CharField(max_length=120)
    brand = models.CharField(max_length=120)
    description = models.TextField(null=True)
    cat = models.ForeignKey(Cat, on_delete=models.CASCADE, related_name='foods')

    class Meta:
        db_table = 'foods'
    
    def __str__(self):
        return f"{self.name} for {self.cat.name}"
    

