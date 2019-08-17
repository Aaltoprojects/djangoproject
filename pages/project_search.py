
def project_search(form):
	start_date = form.cleaned_data['start_date']
	end_date = form.cleaned_data['end_date']
	destination_type = form.cleaned_data['destination_type']
	building_material = form.cleaned_data['building_material']
	service = form.cleaned_data['service']
	construction_operation = form.cleaned_data['construction_operation']
	free_description = form.cleaned_data['free_description']
	project_manager = form.cleaned_data['project_manager']
	return project_manager

