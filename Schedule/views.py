from django.shortcuts import render, get_object_or_404, redirect

from .forms import ScheduleForm
from .models import Schedule
from django.views.generic import UpdateView
# Create your views here.

def schedule_create_view(request):
	form = ScheduleForm(request.POST or None)
	if form.is_valid():
		form.save()
		form = ScheduleForm()
	context = {
		'form' : form
	}
	return render(request, "Schedule/schedule_create.html", context)

def dynamic_lookup_view(request, id):
	obj = Schedule.objects.get(id = id)
	context = {
		"object": obj
	}
	return render(request, "Schedule/schedule_details.html", context)

def list_view(request):
	queryset = Schedule.objects.all()
	context = {
	"object_list": queryset
	}
	return render(request, "Schedule/schedule_list.html", context)

def schedule_delete_view(request, id):
	obj = get_object_or_404(Schedule, id=id)
	if request.method == "POST":
		obj.delete()
		return redirect("../../")
	context = {
		"object": obj
	}
	return render(request, "Schedule/schedule_delete.html", context)

class ScheduleUpdateView(UpdateView):
	template_name = 'schedule_create.html'
	form_class = ScheduleForm
	queryset = Schedule.objects.all()

	def get_object(self):
		id = self.kwargs.get("id")
		return get_object_or_404(Schedule, id=id)

	def form_valid(self, form):
		print(form.cleaned_data)
		return super().form_valid(form)

