from django.test import TestCase
from zoo import models

# Create your tests here.

class AnimalTestCase(TestCase):

    def test_dog_says(self):
        dog = models.Dog(name='Snoopy')
        self.assertEqual(dog.says(), 'Woof')

    def test_cat_says(self):
        cat = models.Cat(name='Garfield')
        self.assertEqual(cat.says(), 'Meow')

    def test_dog_says_error(self):
        dog = models.Dog(name='Snoopy')
        self.assertEqual(dog.says(), 'Woof_error')
