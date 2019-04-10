from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_view(request):
	#return HttpResponse("<h1> Hello World </b></h1>")
	return render(request, "home.html",{})

def dashboard_view(request, *args, **kwargs):
	print(request.user)
	return render(request, "dashboard.html", {})

def about_view(request, *args, **kwargs):
	my_context = {
	"developed_on": "02/03/2019",
	"developed_by": " By ......Still Searching",
	"my_list":[2,0,4,8]
	}
	return render(request, "about.html", my_context)