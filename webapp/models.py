from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class User(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    company_id = models.ForeignKey(Company, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField(max_length=50)

    def __str__(self):
        return self.name

