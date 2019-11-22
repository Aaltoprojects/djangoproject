import datetime
import pages.constants as constants
from django import forms
from django.forms import DateInput
from .widgets import FengyuanChenDatePickerInput

class SearchProjectForm(forms.Form):
    start_date = forms.DateField(required=False, label='Aikaisin lopetuspäivä', help_text="Projektin aloittamispäivämäärä", input_formats=[constants.DATE_FORMAT], widget=FengyuanChenDatePickerInput(attrs={'autocomplete':'off'}))
    end_date = forms.DateField(required=False, label='Myöhäisin aloituspäivä', help_text="Projektin lopettamispäivämäärä",  input_formats=[constants.DATE_FORMAT], widget=FengyuanChenDatePickerInput(attrs={'autocomplete':'off'}))
    structure_type = forms.CharField(required=False,label='Rakennustyyppi', help_text="Projektin kohteen rakennustyyppi", widget=forms.Select(choices=constants.STRUCTURE_TYPES))
    building_material = forms.CharField(required=False,label='Rakennusmateriaali', help_text="Projektin kohteen rakennustyyppi" ,widget=forms.Select(choices=constants.BUILDING_MATERIALS))
    service = forms.CharField(required=False,label='Palvelu', help_text="Projektin kohteen rakennustyyppi", widget=forms.Select(choices=constants.SERVICES))
    construction_operation = forms.CharField(required=False,label='Rakennustoimenpide', help_text="Projektissa tehty rakennustoimenpide", widget=forms.Select(choices=constants.CONSTRUCTION_OPERATIONS))
    key_phrase_search = forms.CharField(required=False,label='Avainsanahaku', help_text="Etsi projekteja syöttämällä hakusanoja", max_length=100,widget=forms.TextInput(attrs={'autocomplete':'off'}))

class CreateProjectForm(forms.Form):
    project_name = forms.CharField(label='Projektin nimi', help_text="Anna projektin nimi", max_length=200,widget=forms.TextInput(attrs={'autocomplete':'off'}))
    destination_name = forms.CharField(label='Kohteen nimi', help_text="Anna kohteen nimi", max_length=200,widget=forms.TextInput(attrs={'autocomplete':'off'}))
    start_date = forms.DateTimeField(label='Aloituspäivä', help_text="Projektin aloittamispäivämäärä", input_formats=[constants.DATE_FORMAT], widget=FengyuanChenDatePickerInput(attrs={'autocomplete':'off'}))
    end_date = forms.DateTimeField(label='Lopetuspäivä', help_text="Projektin lopettamispäivämäärä", input_formats=[constants.DATE_FORMAT], widget=FengyuanChenDatePickerInput(attrs={'autocomplete':'off'}))
    structure_type = forms.CharField(label='Rakennustyyppi', help_text="Projektin kohteen rakennustyyppi", widget=forms.Select(choices=constants.STRUCTURE_TYPES))
    building_material = forms.CharField(label='Rakennusmateriaali', help_text="Projektin kohteen rakennusmateriaali", widget=forms.Select(choices=constants.BUILDING_MATERIALS))
    service = forms.CharField(label='Palvelu', help_text="Projektissa tarjoamamme palvelu", widget=forms.Select(choices=constants.SERVICES))
    construction_operation = forms.CharField(label='Rakennustoimenpide', help_text="Projektin rakennustoimenpide", widget=forms.Select(choices=constants.CONSTRUCTION_OPERATIONS))
    keywords = forms.CharField(label='Avainsanat', required=False, help_text="Anna muutamia avainsanoja, joilla projekti on helppo löytää", empty_value=None,max_length=200,widget=forms.TextInput(attrs={'autocomplete':'off'}))
    project_description = forms.CharField(label='Projektin kuvaus', required=False, help_text="Kuvaile vapaasti projektin sisältöä (max 1000 merkkiä)", empty_value=None,max_length=1000,widget=forms.Textarea(attrs={'cols':50,'rows':5}))
    documentation_path = forms.CharField(label='Polku tiedostojen sijaintiin', required=False, help_text="Kopioi tähän projektikansion polku (esim C:/Ideastructura/Projektit/Projekti-2019)", empty_value=None,max_length=500,widget=forms.TextInput(attrs={'autocomplete':'off'}))
    project_manager = forms.CharField(label='Projektin vetäjä', required=False, help_text="Projektipäällikön nimi", empty_value=None,max_length=100,widget=forms.TextInput(attrs={'autocomplete':'off'}))