from django import forms
from django.db import models
from codes.models import Codes
from exploits.models import Exploits


class Codes(models.Model):
    exploit = models.ForeignKey(Exploits)
    robo = models.ForeignKey(Robo)
    success_url = ('codes/index')