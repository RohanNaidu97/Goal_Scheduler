from django.db import models
from django.urls import reverse

# Create your models here.
class Article(models.Model):
	Task   = models.CharField(max_length=256) #max_length is required
	Deadline = models.DateField()

	def get_absolute_url(self):
		return reverse("article_details", kwargs={"id": self.id})
