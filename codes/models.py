from __future__ import unicode_literals

from django.db import models

class Codes (models.Model):
	name = models.CharField(max_length=120, null=True, blank=True)
	text = models.CharField(max_length=120, null=True, blank=True)
	created = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)
	
def get_absolute_url(self):
        return reverse('detail', kwargs={'pk': self.pk})
