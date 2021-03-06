from __future__ import unicode_literals

import os

from django.apps import apps
from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.utils.translation import gettext
from django.views.decorators.http import require_POST

from .forms import AttachmentForm, ImageForm
from .models import Attachment, Image

def remove_file_from_s3(f):
    f.delete(save=False)

def add_url_for_obj(obj):
    return reverse(
        "attachments:add",
        kwargs={
            "app_label": obj._meta.app_label,
            "model_name": obj._meta.model_name,
            "pk": obj.pk,
        },
    )


def remove_file_from_disk(f):
    if getattr(
        settings, "DELETE_ATTACHMENTS_FROM_DISK", False
    ) and os.path.exists(f.path):
        try:
            os.remove(f.path)
        except OSError:
            pass


@require_POST
@login_required
def add_attachment(
    request,
    app_label,
    model_name,
    pk,
    template_name="attachments/add.html",
    extra_context=None,
):
    next_ = request.POST.get("next", "/")

    if not request.user.has_perm("attachments.add_attachment"):
        return HttpResponseRedirect(next_)

    model = apps.get_model(app_label, model_name)
    obj = get_object_or_404(model, pk=pk)
    attachment_form = AttachmentForm(request.POST, request.FILES)
    image_form = ImageForm(request.POST, request.FILES)

    if attachment_form.is_valid():
        attachment_form.save(request, obj)
        messages.success(request, gettext("Your attachment was uploaded."))
        return HttpResponseRedirect(next_)
    if image_form.is_valid():
        image_form.save(request, obj)
        messages.success(request, gettext("Your image was uploaded."))
        return HttpResponseRedirect(next_)

    template_context = {
        "attachment_form": attachment_form,
        "image_form": image_form,
        "form_url": add_url_for_obj(obj),
        "next": next_,
    }
    template_context.update(extra_context or {})

    return render(request, template_name, template_context)


@login_required
def delete_attachment(request, attachment_pk):
    g = get_object_or_404(Attachment, pk=attachment_pk)
    if (
        request.user.has_perm("attachments.delete_attachment")
        and request.user == g.creator
    ) or request.user.has_perm("attachments.delete_foreign_attachments"):
        remove_file_from_s3(g.attachment_file)
        g.delete()
        messages.success(request, gettext("Your attachment was deleted."))
    next_ = request.GET.get("next") or "/"
    return HttpResponseRedirect(next_)

@login_required
def delete_image(request, attachment_pk):
    g = get_object_or_404(Image, pk=attachment_pk)
    if (
        request.user.has_perm("attachments.delete_attachment")
        and request.user == g.creator
    ) or request.user.has_perm("attachments.delete_foreign_attachments"):
        remove_file_from_s3(g.attachment_image)
        g.delete()
        messages.success(request, gettext("Your image was deleted."))
    next_ = request.GET.get("next") or "/"
    return HttpResponseRedirect(next_)
