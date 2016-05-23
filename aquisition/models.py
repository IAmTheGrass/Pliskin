from __future__ import unicode_literals

from django.db import models

from exploits.models import Exploits
from robo.models import Robo

class Aquisition (models.Model):
	exploit = models.ForeignKey(Exploits)
	robo = models.ForeignKey(Robo)
	created = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)
	
def get_absolute_url(self):
        return reverse('detail', kwargs={'pk': self.pk})
