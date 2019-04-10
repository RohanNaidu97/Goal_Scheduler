from django import forms

from .models import Article

class Articleform(forms.ModelForm):
	Deadline = forms.DateField(required = False, input_formats = ['%d-%m-%y'])
	class Meta:
		model  = Article
		fields = [
		'Task',
		'Deadline',
		]