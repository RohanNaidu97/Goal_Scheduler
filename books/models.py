from django.db import models
from django.urls import reverse


# Create your models here.
class books(models.Model):
	Title  = models.CharField(max_length=120) #max_length is required
	Status = models.TextField(blank=True, null=True)
	#Completed = models.BooleanField()

	def get_absolute_url(self):
		return  reverse("books_details", kwargs={"id": self.id}) #f"/books/{self.id}/"