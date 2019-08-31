from formtools.preview import FormPreview
from django.http import HttpResponseRedirect
from pages.models import Project

class SomeModelFormPreview(FormPreview):

    def done(self, request, cleaned_data):
        # Do something with the cleaned_data, then redirect
        # to a "success" page.
        return HttpResponseRedirect('/success')