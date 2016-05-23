from __future__ import unicode_literals
from django.core.urlresolvers import reverse

from django.db import models

class Robo (models.Model):
	name = models.CharField(max_length=120, null=True, blank=True)
	tribe = models.CharField(max_length=120, null=True, blank=True)
	created = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)
	
def get_absolute_url(self):
        return reverse('detail', kwargs={'pk': self.pk})
