from django import generic
from .models import Project

class ListView(generic.ListView)
    model = Project
    template_name = 'todas.html'