from __future__ import unicode_literals

from django.conf.urls import url

from .views import add_attachment, delete_attachment, delete_image

app_name = "attachments"

urlpatterns = [
    url(
        r"^add-for/(?P<app_label>[\w\-]+)/(?P<model_name>[\w\-]+)/(?P<pk>\d+)/$",
        add_attachment,
        name="add",
    ),
    url(r"^delete/attachment/(?P<attachment_pk>\d+)/$", delete_attachment, name="delete_attachment"),
    url(r"^delete/image/(?P<attachment_pk>\d+)/$", delete_image, name="delete_image"),
]
