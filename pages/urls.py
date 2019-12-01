from django.urls import path
from django.conf.urls import url, include
from . import views
import re

urlpatterns = [
	path('', views.home, name='home'),
    path('', include('django.contrib.auth.urls')),
    url(r'^signup/$', views.signup, name='signup'),
    path('confirm', views.confirmUser, name='User confirmed'),
    path('logout/', views.logout, name='logout'),
	path('post/', views.add_project, name='add_project'),
	path('success', views.post_success),
	path('add_filter', views.add_filter, name='add_filter'),
]