from django import forms

from .models import Dolist

class DolistForm(forms.ModelForm):
	class Meta:
		model = Dolist
		fields = [
		'Todo',
		'Description'
		]