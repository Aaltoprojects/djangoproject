from django.contrib import admin
from django.contrib.auth.models import Group
import pages.models

admin.site.register(pages.models.Project)
admin.site.register(pages.models.UploadFilesModel)
admin.site.register(pages.models.Filter)
admin.site.register(pages.models.ReferenceProject)
admin.site.site_header = 'Projektipankin ylläpito'
admin.site.unregister(Group)