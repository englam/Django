from django.db import models

# Create your models here.

class Animal(models.Model):

    name = models.CharField(max_length=256)

    def says(self):
        raise NotImplementedError("I do not know")

    class Meta:
        abstract = True


class Dog(Animal):

    def says(self):
        return ("Woof")

class Cat(Animal):

    def says(self):
        return ("Meow")




