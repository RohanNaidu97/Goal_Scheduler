from django.shortcuts import render, get_object_or_404, redirect

from .forms import DolistForm
from .models import Dolist
from django.views.generic import UpdateView
# Create your views here.

def dolist_create_view(request):
	form = DolistForm(request.POST or None)
	if form.is_valid():
		form.save()
		form = DolistForm()
	context = {
		'form' : form
	}
	return render(request, "Dolist/dolist_create.html", context)

def dynamic_lookup_view(request, id):
	obj = Dolist.objects.get(id = id)
	context = {
		"object": obj
	}
	return render(request, "Dolist/dolist_details.html", context)

def list_view(request):
	queryset = Dolist.objects.all()
	context = {
	"object_list": queryset
	}
	return render(request, "Dolist/dolist_list.html", context)

def dolist_delete_view(request, id):
	obj = get_object_or_404(Dolist, id=id)
	if request.method == "POST":
		obj.delete()
		return redirect("../../")
	context = {
		"object": obj
	}
	return render(request, "Dolist/dolist_delete.html", context)

class DolistUpdateView(UpdateView):
	template_name = 'dolist_create.html'
	form_class = DolistForm
	queryset = Dolist.objects.all()

	def get_object(self):
		id = self.kwargs.get("id")
		return get_object_or_404(Dolist, id=id)

	def form_valid(self, form):
		print(form.cleaned_data)
		return super().form_valid(form)

