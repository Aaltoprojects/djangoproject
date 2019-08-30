from django.urls import path
from . import views

urlpatterns = [
	path('', views.home, name = 'home'),
	path('luo', views.create_project, name = 'add_project'),
	path('lisaamonta', views.add_entries_to_db, name = 'add_entries'),
]