from formtools.preview import FormPreview
from django.http import HttpResponseRedirect
from pages.models import Project

class SomeModelFormPreview(FormPreview):

    def done(self, request, cleaned_data):
        # Do something with the cleaned_data, then redirect
        # to a "success" page.
        instance = Project(
			project_name = cleaned_data['project_name'],
			destination_name = cleaned_data['destination_name'],
			start_date = cleaned_data['start_date'],
			end_date = cleaned_data['end_date'],
			structure_type = cleaned_data['structure_type'],
			building_material = cleaned_data['building_material'],
			service = cleaned_data['service'],
			construction_operation = cleaned_data['construction_operation'],
			specific_project_type = cleaned_data['specific_project_type'],
			project_description = cleaned_data['project_description'],
			documentation_path = cleaned_data['documentation_path'],
			project_manager = cleaned_data['project_manager'],
			)
        instance.save()
        return HttpResponseRedirect('/success')