# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

category_choices = (
    ('arts','Arts'),
    ('development','Development'),

)

class Category(models.Model):
    name = models.CharField(max_length=255)


# Create your models here.
class Inputs(models.Model):
    text = models.CharField(max_length=255)
    number = models.IntegerField()
    select = models.CharField(max_length=255,choices=category_choices)
    checkbox = models.BooleanField()
    date = models.DateField()
    time = models.TimeField()
    datetime = models.DateTimeField()
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    url = models.URLField(max_length=200)
    email = models.EmailField()
    file = models.FileField(upload_to='uploads/')
