from django.urls import path
from . import views

urlpatterns = [
	path('', views.home, name = 'home'),
	path('csearch', views.companysearch, name = 'companysearch'),
	path('search/', views.search, name = 'search'),
	path('create/', views.create, name = 'create'),
]