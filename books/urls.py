from django.urls import path

from books.views import *

urlpatterns = [
	path('', books_list_view, name='books_list'),
	path('<int:id>/', dynamic_lookup_view, name='books_details'),
	path('create/', books_create_view, name='books_create'),
	path('<int:id>/delete/', books_delete_view, name='books_delete'),
]