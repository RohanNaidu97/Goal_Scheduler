from django.db import models
from django.urls import reverse

# Create your models here.
class Schedule(models.Model):
	Jobs = models.CharField(max_length=256)
	Time = models.TimeField()

	def get_absolute_url(self):
		return reverse("schedule_details", kwargs={"id":self.id})