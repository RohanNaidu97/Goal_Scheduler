from django.db import models
from django.urls import reverse

# Create your models here.
class Dolist(models.Model):
	Todo = models.CharField(max_length=128)
	Description = models.CharField(max_length=256)

	def get_absolute_url(self):
		return reverse("dolist_details", kwargs={"id":self.id})