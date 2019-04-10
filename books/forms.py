from django import forms

from .models import books

class booksform(forms.ModelForm):
	class Meta:
		model = books
		fields = [
		'Title',
		'Status'	
		]


class RawBooksForm(forms. Form):
	Title  = forms.CharField()
	Status = forms.CharField(initial='Not Started Yet')