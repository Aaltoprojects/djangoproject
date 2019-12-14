import datetime
import pages.constants as constants
from pages.models import Filter
from django import forms
from django.forms import DateInput
from .widgets import FengyuanChenDatePickerInput


class SearchProjectForm(forms.Form):

    start_date = forms.DateField(
        label='Aikaisin lopetuspäivä',
        required=False,
        input_formats=[constants.DATE_FORMAT],
        widget=FengyuanChenDatePickerInput(attrs={
                                                'placeholder': 'Projektin aloittamispäivämäärä',
                                                'autocomplete': 'off',
                                                }
        ),
    )
    end_date = forms.DateField(
        label='Myöhäisin aloituspäivä',
        required=False,
        input_formats=[constants.DATE_FORMAT],
        widget=FengyuanChenDatePickerInput(attrs={
                                                'placeholder': 'Projektin lopettamispäivämäärä',
                                                'autocomplete': 'off',
                                                }
        ),
    )
    key_phrase_search = forms.CharField(
        label='Avainsanahaku',
        required=False,
        max_length=100,
        widget=forms.TextInput(attrs={
                                    'placeholder': 'Etsi projekteja syöttämällä hakusanoja', 
                                    'autocomplete': 'off'
                                    }
        ),
    )


class CreateProjectForm(forms.Form):

    project_name = forms.CharField(
        label='Projektin nimi',
        empty_value='—',
        max_length=200,
        widget=forms.TextInput(attrs={
                                    'placeholder': 'Anna projektin nimi', 
                                    'autocomplete': 'off'
                                    }
        ),
    )
    destination_name = forms.CharField(
        label='Kohteen nimi',
        required=False,
        empty_value='—',
        max_length=200,
        widget=forms.TextInput(attrs={
                                    'placeholder': 'Anna kohteen nimi', 
                                    'autocomplete': 'off'
                                    }
        ),
    )
    start_date = forms.DateTimeField(
        label='Aloituspäivä',
        required=False,
        input_formats=[constants.DATE_FORMAT],
        widget=FengyuanChenDatePickerInput(attrs={
                                                'placeholder': 'Projektin aloittamispäivämäärä',
                                                'autocomplete': 'off',
                                                }
        ),
    )
    end_date = forms.DateTimeField(
        label='Lopetuspäivä',
        required=False,
        input_formats=[constants.DATE_FORMAT],
        widget=FengyuanChenDatePickerInput(attrs={
                                                'placeholder': 'Projektin lopettamispäivämäärä',
                                                'autocomplete': 'off',
                                                }
        ),
    )
    keywords = forms.CharField(
        label='Avainsanat',
        required=False,
        empty_value='—',
        max_length=200,
        widget=forms.TextInput(attrs={
                                    'placeholder': 'Anna muutamia avainsanoja, joilla projekti on helppo löytää', 
                                    'autocomplete': 'off'
                                    }
        ),
    )
    project_description = forms.CharField(
        label='Projektin kuvaus',
        empty_value='—',
        max_length=5000,
        widget=forms.Textarea(attrs={
                                    'cols': 50,
                                    'rows': 5,
                                    'placeholder': 'Kuvaile vapaasti projektin sisältöä (max 1000 merkkiä)',
                                    }
        ),
    )
    documentation_path = forms.CharField(
        label='Polku tiedostojen sijaintiin',
        required=False,
        empty_value='—',
        max_length=500,
        widget=forms.TextInput(attrs={
                                    'placeholder': 'Kopioi tähän projektikansion polku (esim C:/Ideastructura/Projektit/Projekti-2019)', 
                                    'autocomplete': 'off'
                                    }
        ),
    )
    project_manager = forms.CharField(
        label='Projektin vetäjä',
        required=False,
        empty_value='—',
        max_length=100,
        widget=forms.TextInput(attrs={
                                    'placeholder': 'Projektipäällikön nimi', 
                                    'autocomplete': 'off'
                                    }
        ),
    )


class AddFilterForm(forms.ModelForm):

    class Meta:
        model = Filter
        fields = ['category', 'filter_name']
