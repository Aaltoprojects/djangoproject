from django.contrib import admin
from django.contrib.auth.models import Group
import pages.models
from attachments.admin import AttachmentInlines
from attachments.models import Attachment

admin.site.register(pages.models.Project)
admin.site.register(pages.models.Filter)
admin.site.register(pages.models.ReferenceProject)
admin.site.site_header = 'Projektipankin ylläpito'
admin.site.unregister(Group)

class MyEntryOptions(admin.ModelAdmin):
    inlines = (AttachmentInlines,)

admin.site.register(Attachment, MyEntryOptions)