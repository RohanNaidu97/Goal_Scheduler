from django.urls import path

from Schedule.views import *

urlpatterns = [
	path('', list_view, name='schedule_list'),
	path('<int:id>/', dynamic_lookup_view, name='schedule_details'),
	path('create/', schedule_create_view, name='schedule_create'),
	path('<int:id>/delete/', schedule_delete_view, name='schedule_delete'),
	path('<int:id>/update/', ScheduleUpdateView.as_view(), name='schedule_update'),
]