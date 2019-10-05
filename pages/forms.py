import datetime
import pages.constants as constants
from django import forms
from django.forms import DateInput
from .widgets import FengyuanChenDatePickerInput

class SearchProjectForm(forms.Form):
    start_date = forms.DateField(required=False, label='Aikaisin lopetuspäivä', input_formats=[constants.DATE_FORMAT], widget=FengyuanChenDatePickerInput(attrs={'autocomplete':'off'}))
    end_date = forms.DateField(required=False, label='Myöhäisin aloituspäivä', input_formats=[constants.DATE_FORMAT], widget=FengyuanChenDatePickerInput(attrs={'autocomplete':'off'}))
    structure_type = forms.CharField(required=False,label='Rakennustyyppi',widget=forms.Select(choices=constants.STRUCTURE_TYPES))
    building_material = forms.CharField(required=False,label='Rakennusmateriaali',widget=forms.Select(choices=constants.BUILDING_MATERIALS))
    service = forms.CharField(required=False,label='Palvelu',widget=forms.Select(choices=constants.SERVICES))
    construction_operation = forms.CharField(required=False,label='Rakennustoimenpide',widget=forms.Select(choices=constants.CONSTRUCTION_OPERATIONS))
    key_phrase_search = forms.CharField(required=False,label='Avainsanahaku',max_length=100,widget=forms.TextInput(attrs={'autocomplete':'off'}))

class CreateProjectForm(forms.Form):
    project_name = forms.CharField(label='Projektin nimi',max_length=200,widget=forms.TextInput(attrs={'autocomplete':'off'}))
    destination_name = forms.CharField(label='Kohteen nimi',max_length=200,widget=forms.TextInput(attrs={'autocomplete':'off'}))
    start_date = forms.DateTimeField(label='Aloituspäivä', input_formats=[constants.DATE_FORMAT], widget=FengyuanChenDatePickerInput(attrs={'autocomplete':'off'}))
    end_date = forms.DateTimeField(label='Lopetuspäivä', input_formats=[constants.DATE_FORMAT], widget=FengyuanChenDatePickerInput(attrs={'autocomplete':'off'}))
    structure_type = forms.CharField(label='Rakennustyyppi',widget=forms.Select(choices=constants.STRUCTURE_TYPES[1:]))
    building_material = forms.CharField(label='Rakennusmateriaali',widget=forms.Select(choices=constants.BUILDING_MATERIALS[1:]))
    service = forms.CharField(label='Palvelu',widget=forms.Select(choices=constants.SERVICES[1:]))
    construction_operation = forms.CharField(label='Rakennustoimenpide',widget=forms.Select(choices=constants.CONSTRUCTION_OPERATIONS[1:]))
    keywords = forms.CharField(required=False,empty_value=None,label='Avainsanat',max_length=200,widget=forms.TextInput(attrs={'autocomplete':'off'}))
    project_description = forms.CharField(required=False,empty_value=None,label='Projektin kuvaus',max_length=500,widget=forms.Textarea(attrs={'cols':50,'rows':5}))
    documentation_path = forms.CharField(required=False,empty_value=None,label='Polku tiedostojen sijaintiin',max_length=200,widget=forms.TextInput(attrs={'autocomplete':'off'}))
    project_manager = forms.CharField(required=False,empty_value=None,label='Projektin vetäjä',max_length=100,widget=forms.TextInput(attrs={'autocomplete':'off'}))