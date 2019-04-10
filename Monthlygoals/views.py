from django.shortcuts import render

from .forms import Articleform
from .models import Article
# Create your views here.

def article_create_view(request):
	form = Articleform(request.POST or None)
	if form.is_valid():
		form.save()
		form = Articleform()
	context = {
		'form' : form
	}
	return render(request, "Monthlygoals/article_create.html", context)

def dynamic_lookup_view(request, id):
	obj = Article.objects.get(id = id)
	context = {
		"object": obj
	}
	return render(request, "Monthlygoals/article_details.html", context)

def list_view(request):
	queryset = Article.objects.all()
	context = {
	"object_list": queryset
	}
	return render(request, "Monthlygoals/article_list.html", context)

def article_delete_view(request, id):
	obj = get_object_or_404(Article, id=id)
	if request.method == "POST":
		obj.delete()
		return redirect("../../")
	context = {
		"object": obj
	}
	return render(request, "Monnthlygoals/article_delete.html", context)