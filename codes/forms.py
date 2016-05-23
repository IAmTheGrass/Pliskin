from django import forms
from django.db import models


class Codes(models.Model):
    name = models.CharField(max_length=200)
    text = models.CharField(max_length=200)
    success_url = ('codes/index')