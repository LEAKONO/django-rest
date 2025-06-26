from django.db import models

# Create your models here.
class Person(models.Model):
    name=models.CharField(max_length=100)
    age=models.IntegerField()
    isStudent=models.BooleanField(default=True)
    def __str__(self):
        return self.name