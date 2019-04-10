from django.shortcuts import render

from .forms import booksform, RawBooksForm
from .models import books
# Create your views here.
'''
def books_create_view(request):
	my_form = RawBooksForm()
	if request.method == "POST":
		my_form = RawBooksForm(request.POST)
		if my_form.is_valid():
			print(my_form.cleaned_data)
			books.objects.create(**my_form.cleaned_data)
		else:
			print(my_form.errors)
	context ={
		"form": my_form
	}
	return render(request, "books/books_create.html", context)
'''
def books_create_view(request):
	form = booksform(request.POST or None)
	if form.is_valid():
		form.save()
		form = booksform()

	context = {
		'form': form
	}
	return render(request, "books/books_create.html",context)

def books_details_view(request):
	obj = books.objects.get(id=1)
	context = {
	'title'  : obj.Title,
	'status' : obj.Status
	}
	return render(request, "books/books_details.html", context)

def dynamic_lookup_view(request, id ):
	obj=books.objects.get(id = id)
	context = {
		"object":obj
	}
	return render(request,"books/books_details.html", context)

def books_list_view(request):
	queryset = books.objects.all()
	context = {
	"object_list": queryset
	}
	return render(request, "books/books_list.html", context)

def books_delete_view(request, id):
	obj = get_object_or_404(books, id=id)
	if request.method == "POST":
		obj.delete()
		return redirect("../../")
	context = {
		"object": obj
	}
	return render(request, "books/books_delete.html", context)