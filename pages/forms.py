import datetime
import pages.constants as constants
from django import forms

class SearchProjectForm(forms.Form):
    start_date = forms.DateField(required=False,label='Aloitus pvm',widget=forms.SelectDateWidget(empty_label="-",years=constants.YEARS))
    end_date = forms.DateField(required=False,label='Lopetus pvm',widget=forms.SelectDateWidget(empty_label="-",years=constants.YEARS))
    structure_type = forms.CharField(required=False,label='Rakennustyyppi',widget=forms.Select(choices=constants.STRUCTURE_TYPES))
    building_material = forms.CharField(required=False,label='Rakennusmateriaali',widget=forms.Select(choices=constants.BUILDING_MATERIALS))
    service = forms.CharField(required=False,label='Palvelu',widget=forms.Select(choices=constants.SERVICES))
    construction_operation = forms.CharField(required=False,label='Rakennustoimenpide',widget=forms.Select(choices=constants.CONSTRUCTION_OPERATIONS))
    project_manager = forms.CharField(required=False,label='Projektin vetäjä',max_length=100)

class CreateProject(forms.Form):
    project_name = forms.CharField(label='Projektin nimi',max_length=200)
    destination_name = forms.CharField(label='Kohteen nimi',max_length=200)
    start_date = forms.DateField(required=False,label='Aloitus pvm',widget=forms.SelectDateWidget(empty_label="-",years=constants.YEARS))
    end_date = forms.DateField(required=False,label='Lopetus pvm',widget=forms.SelectDateWidget(empty_label="-",years=constants.YEARS))
    structure_type = forms.CharField(label='Rakennustyyppi',widget=forms.Select(choices=constants.STRUCTURE_TYPES[1:]))
    building_material = forms.CharField(label='Rakennusmateriaali',widget=forms.Select(choices=constants.BUILDING_MATERIALS[1:]))
    service = forms.CharField(label='Palvelu',widget=forms.Select(choices=constants.SERVICES[1:]))
    construction_operation = forms.CharField(label='Rakennustoimenpide',widget=forms.Select(choices=constants.CONSTRUCTION_OPERATIONS[1:]))
    specific_project_type = forms.CharField(required=False,label='Osaamisalue',max_length=200)
    project_manager = forms.CharField(required=False,label='Projektin vetäjä',max_length=100)
    project_description = forms.CharField(required=False,label='Projektin kuvaus',max_length=500,widget=forms.Textarea(attrs={'cols':50,'rows':5}))
    documentation_path = forms.CharField(label='Polku tiedostojen sijaintiin',max_length=200)