from __future__ import unicode_literals

import os

from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.utils.translation import gettext_lazy as _
from six import python_2_unicode_compatible


def attachment_upload(instance, filename):
    """Stores the attachment in a "per module/appname/primary key" folder"""
    return "{app}_{model}/attachments/{pk}/{filename}".format(
        app=instance.content_object._meta.app_label,
        model=instance.content_object._meta.object_name.lower(),
        pk=instance.content_object.pk,
        filename=filename,
    )

def image_upload(instance, filename):
    """Stores the attachment in a "per module/appname/primary key" folder"""
    return "{app}_{model}/images/{pk}/{filename}".format(
        app=instance.content_object._meta.app_label,
        model=instance.content_object._meta.object_name.lower(),
        pk=instance.content_object.pk,
        filename=filename,
    )


class AttachmentManager(models.Manager):
    def attachments_for_object(self, obj):
        object_type = 8
        #object_type = ContentType.objects.get_for_model(obj)
        return self.filter(content_type__pk=object_type, object_id=obj)


@python_2_unicode_compatible
class Attachment(models.Model):
    objects = AttachmentManager()

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey("content_type", "object_id")
    creator = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name="created_attachments",
        verbose_name=_("creator"),
        on_delete=models.CASCADE,
    )
    attachment_file = models.FileField(
        _("attachment"), upload_to=attachment_upload
    )
    created = models.DateTimeField(_("created"), auto_now_add=True)
    modified = models.DateTimeField(_("modified"), auto_now=True)

    class Meta:
        verbose_name = _("attachment")
        verbose_name_plural = _("attachments")
        ordering = ["-created"]
        permissions = (
            ("delete_foreign_attachments", _("Can delete foreign attachments")),
        )

    def __str__(self):
        return _("{username} attached {filename}").format(
            username=self.creator.get_username(),
            filename=self.attachment_file.name,
        )

    @property
    def filename(self):
        return os.path.split(self.attachment_file.name)[1]


@python_2_unicode_compatible
class Image(models.Model):
    objects = AttachmentManager()

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey("content_type", "object_id")
    creator = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name="created_images",
        verbose_name=_("creator"),
        on_delete=models.CASCADE,
    )
    attachment_image = models.ImageField(
        _("image"), upload_to=image_upload
    )
    created = models.DateTimeField(_("created"), auto_now_add=True)
    modified = models.DateTimeField(_("modified"), auto_now=True)

    class Meta:
        verbose_name = _("image")
        verbose_name_plural = _("images")
        ordering = ["-created"]
        permissions = (
            ("delete_foreign_images", _("Can delete foreign images")),
        )

    def __str__(self):
        return _("{username} attached {filename}").format(
            username=self.creator.get_username(),
            filename=self.attachment_image.name,
        )

    @property
    def filename(self):
        return os.path.split(self.attachment_image.name)[1]
