from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.models.CharField(max_length=150)

    def __str__(self):
        return self.name