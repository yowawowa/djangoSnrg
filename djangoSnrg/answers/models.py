from django.db import models
from django.urls import reverse_lazy


# Create your models here.
class Answer(models.Model):
    lesson = models.CharField(max_length=50)
    question = models.TextField()
    answer = models.TextField(blank=True)


class Human(models.Model):
    name = models.CharField(max_length=40)
    height = models.IntegerField(null=True)
    address = models.CharField(max_length=100)
    description = models.CharField(max_length=300, null=True, blank=True, default='description here')
    photo = models.ImageField(upload_to='media/%Y/%m/%d', null=True, blank=True, default='')
    profession = models.ForeignKey('Profession', on_delete=models.PROTECT, null=True, blank=True)

    def get_absolute_url(self):
        return reverse_lazy('View_human', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = 'Human'
        verbose_name_plural = 'Humans'


class Profession(models.Model):
    title = models.CharField(max_length=40)

    # TODO kwargs
    def get_absolute_url(self):
        return reverse_lazy('Profession', kwargs={'profession_id': self.pk})

    class Meta:
        verbose_name = 'Profession'
        verbose_name_plural = 'Professions'
        ordering = ['title']
