from django.contrib import admin
from django.contrib.auth.models import Group
import pages.models

admin.site.register(pages.models.Project)
admin.site.site_header = 'Osaamispankki Administration'
admin.site.unregister(Group)