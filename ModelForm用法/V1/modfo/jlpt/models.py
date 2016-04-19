#coding:utf8

from django.db import models

# Create your models here.
LEVEL_CHOICES = (
    ('N1', 'N1'),
    ('N2', 'N2'),
    ('N3', 'N3'),
    ('N4', 'N4'),
    ('N5', 'N5'),
    ('NO', 'NO'),
)
class ExamInfo(models.Model):
    name = models.CharField(max_length=10)
    level = models.CharField(max_length=2, choices=LEVEL_CHOICES)