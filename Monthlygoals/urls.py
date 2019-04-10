from django.urls import path

from Monthlygoals.views import article_create_view, dynamic_lookup_view, list_view

urlpatterns = [
	path('', list_view, name= 'article_list'),
	path('<int:id>/', dynamic_lookup_view, name='article_details'),
	path('create/' , article_create_view, name='article_create'),

]