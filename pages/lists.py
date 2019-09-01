from django import generic
import models

class ListView(generic.ListView)
    model = models.Project
    template_name = 'todas.html'