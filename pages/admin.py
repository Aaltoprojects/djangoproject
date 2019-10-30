from django.contrib import admin
from django.contrib.auth.models import Group
import pages.models

admin.site.register(pages.models.Project)
admin.site.site_header = 'Osaamispankki Administration testi'
admin.site.unregister(Group)