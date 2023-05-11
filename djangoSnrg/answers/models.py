from django.db import models

# Create your models here.
class Answer(models.Model):
    lesson = models.CharField(max_length=50)
    question = models.TextField()
    answer = models.TextField(blank=True)


class Human(models.Model):
    name = models.CharField(max_length=40)
    height = models.IntegerField(null=True)
    address = models.CharField(max_length=100)
