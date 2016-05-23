from django import forms
from django.db import models


class Robo(models.Model):
    name = models.CharField(max_length=200)
    tribe = models.CharField(max_length=200)
    success_url = ('robo/index')

