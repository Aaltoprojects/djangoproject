import datetime
import pages.constants as constants
import pages.models as models
from django import forms
from django.forms import DateInput
from .widgets import FengyuanChenDatePickerInput

class SearchProjectForm(forms.Form):

    def format_qset(self, data_qs):
        array = []
        for filter in data_qs:
            name = filter.filter_name
            tup = (name, name)
            array.append(tup)
        return array

    def get_filters(self):
        f1 = self.format_qset(models.Filter.filter_db.all().filter(category='Rakennustyyppi'))
        f2 = self.format_qset(models.Filter.filter_db.all().filter(category='Rakennusmateriaali'))
        f3 = self.format_qset(models.Filter.filter_db.all().filter(category='Palvelu'))
        f4 = self.format_qset(models.Filter.filter_db.all().filter(category='Rakennustoimenpide'))
        f5 = self.format_qset(models.Filter.filter_db.all().filter(category='Rakenneosa'))
        return [f1,f2,f3,f4,f5]

    def __init__(self, *args, **kwargs):
        super(SearchProjectForm, self).__init__(*args, **kwargs)
        self.fields['structure_type'] = forms.CharField(
                                            label='Rakennustyyppi',
                                            required=False,
                                            help_text="Projektin kohteen rakennustyyppi",
                                            widget=forms.Select(choices=self.get_filters()[0])
                                        )
        self.fields['building_material'] = forms.CharField(
                                            label='Rakennusmateriaali',
                                            required=False,
                                            help_text="Projektin kohteen rakennustyyppi",
                                            widget=forms.Select(choices=self.get_filters()[1])
                                        )
        self.fields['service'] = forms.CharField(
                                            label='Palvelu',
                                            required=False,
                                            help_text="Projektin kohteen rakennustyyppi",
                                            widget=forms.Select(choices=self.get_filters()[2])
                                        )
        self.fields['construction_operation'] = forms.CharField(
                                            label='Rakennustoimenpide',
                                            required=False,
                                            help_text="Projektissa tehty rakennustoimenpide",
                                            widget=forms.Select(choices=self.get_filters()[3])
                                        )
        self.fields['structural_component'] = forms.CharField(
                                            label='Rakenneosa',
                                            required=False,
                                            help_text="Projektin rakenneosa",
                                            empty_value='—',
                                            widget=forms.Select(choices=self.get_filters()[4])
                                        )
    start_date = forms.DateField(
        label='Aikaisin lopetuspäivä',
        required=False,
        help_text="Projektin aloittamispäivämäärä",
        input_formats=[constants.DATE_FORMAT],
        widget=FengyuanChenDatePickerInput(attrs={'autocomplete':'off'})
    )
    end_date = forms.DateField(
        label='Myöhäisin aloituspäivä',
        required=False,
        help_text="Projektin lopettamispäivämäärä",
        input_formats=[constants.DATE_FORMAT],
        widget=FengyuanChenDatePickerInput(attrs={'autocomplete':'off'})
    )
    key_phrase_search = forms.CharField(
        label='Avainsanahaku',
        required=False,
        help_text="Etsi projekteja syöttämällä hakusanoja",
        max_length=100,
        widget=forms.TextInput(attrs={'autocomplete':'off'})
    )

class CreateProjectForm(forms.Form):
    project_name = forms.CharField(
        label='Projektin nimi',
        required=True,
        help_text="Anna projektin nimi",
        empty_value='—',
        max_length=200,
        widget=forms.TextInput(attrs={'autocomplete':'off'})
    )
    destination_name = forms.CharField(
        label='Kohteen nimi',
        required=False,
        help_text="Anna kohteen nimi",
        empty_value='—',
        max_length=200,
        widget=forms.TextInput(attrs={'autocomplete':'off'})
    )
    start_date = forms.DateTimeField(
        label='Aloituspäivä',
        required=False,
        help_text="Projektin aloittamispäivämäärä",
        input_formats=[constants.DATE_FORMAT],
        widget=FengyuanChenDatePickerInput(attrs={'autocomplete':'off'})
    )
    end_date = forms.DateTimeField(
        label='Lopetuspäivä',
        required=False,
        help_text="Projektin lopettamispäivämäärä",
        input_formats=[constants.DATE_FORMAT],
        widget=FengyuanChenDatePickerInput(attrs={'autocomplete':'off'})
    )
    structure_type = forms.CharField(
        label='Rakennustyyppi',
        required=False,
        help_text="Projektin kohteen rakennustyyppi",
        empty_value='—',
        widget=forms.Select(choices=constants.FILTER_CATEGORIES)
    )
    building_material = forms.CharField(
        label='Rakennusmateriaali',
        required=False,
        help_text="Projektin kohteen rakennusmateriaali",
        empty_value='—',
        widget=forms.Select(choices=constants.FILTER_CATEGORIES)
    )
    service = forms.CharField(
        label='Palvelu',
        required=False,
        help_text="Projektissa tarjoamamme palvelu",
        empty_value='—',
        widget=forms.Select(choices=constants.FILTER_CATEGORIES)
    )
    construction_operation = forms.CharField(
        label='Rakennustoimenpide',
        required=False,
        help_text="Projektin rakennustoimenpide",
        empty_value='—',
        widget=forms.Select(choices=constants.FILTER_CATEGORIES)
    )
    structural_component = forms.CharField(
        label='Rakenneosa',
        required=False,
        help_text="Projektin rakenneosa",
        empty_value='—',
        widget=forms.Select(choices=constants.FILTER_CATEGORIES)
    )
    keywords = forms.CharField(
        label='Avainsanat',
        required=False,
        help_text="Anna muutamia avainsanoja, joilla projekti on helppo löytää",
        empty_value='—',
        max_length=200,
        widget=forms.TextInput(attrs={'autocomplete':'off'})
    )
    project_description = forms.CharField(
        label='Projektin kuvaus',
        required=False,
        help_text="Kuvaile vapaasti projektin sisältöä (max 1000 merkkiä)",
        empty_value='—',
        max_length=1000,
        widget=forms.Textarea(attrs={'cols':50,'rows':5})
    )
    documentation_path = forms.CharField(
        label='Polku tiedostojen sijaintiin',
        required=False,
        help_text="Kopioi tähän projektikansion polku (esim C:/Ideastructura/Projektit/Projekti-2019)",
        empty_value='—',
        max_length=500,
        widget=forms.TextInput(attrs={'autocomplete':'off'})
    )
    project_manager = forms.CharField(
        label='Projektin vetäjä',
        required=False,
        help_text="Projektipäällikön nimi",
        empty_value='—',
        max_length=100,
        widget=forms.TextInput(attrs={'autocomplete':'off'})
    )

class AddFilterForm(forms.ModelForm):

    class Meta:
        model = models.Filter
        fields = ['category', 'filter_name']