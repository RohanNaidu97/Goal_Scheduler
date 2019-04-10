from django.urls import path

from Dolist.views import *

urlpatterns = [
	path('', list_view, name='dolist_list'),
	path('<int:id>/', dynamic_lookup_view, name='dolist_details'),
	path('create/', dolist_create_view, name='dolist_create'),
	path('<int:id>/delete/', dolist_delete_view, name='dolist_delete'),
	path('<int:id>/update/', DolistUpdateView.as_view(), name='dolist_update'),
]