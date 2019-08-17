import datetime
import pages.constants as constants
from django import forms

#Nämä on esimerkkeinä tässä, siitä miten formeja tehdään, ei vissiin käytetä vielä tässä vaiheessa kun ei ole työntekijöitä kannassa t. Amos

#Company search form
class NameForm(forms.Form):
    coname = forms.CharField(label='Company name', max_length=100)
    coid = forms.CharField(label='Company ID', max_length=100)

#Employee search form
class create_employee_form(forms.Form):
	
    fname = forms.CharField(label='First name', max_length=100)
    surname = forms.CharField(label='Surname', max_length=100)
    title = forms.CharField(label='Title', max_length=100)
    function = forms.CharField(label='Function', max_length=100)
    siivous = forms.IntegerField(label='Siivous')
    tetsaus = forms.IntegerField(label='Tetsaus')
    johtaminen = forms.IntegerField(label='Johtaminen')

class search_form(forms.Form):
    search_field = forms.CharField(label='Search employees', max_length=100)

class SearchProjectForm(forms.Form):
    start_date = forms.DateField(initial=datetime.date.today)
    end_date = forms.DateField(initial=datetime.date.today)
    destination_type = forms.CharField(label='Rakennustyyppi', widget=forms.Select(choices=constants.DESTINATION_TYPES))
    building_material = forms.CharField(label='Rakennusmateriaali', widget=forms.Select(choices=constants.BUILDING_MATERIALS))
    service = forms.CharField(label='Palvelu', widget=forms.Select(choices=constants.SERVICES))
    construction_operation = forms.CharField(label='Rakennustoimenpide', widget=forms.Select(choices=constants.CONSTRUCTION_OPERATIONS))
    free_description = forms.CharField(label='Vapaa hakukenttä', max_length=100)
    project_manager = forms.CharField(label='Projektin vetäjä', max_length=100)

class Create_project(forms.Form):
    project_name = forms.CharField(label='Projektin nimi', max_length='200')
    destination_name = forms.CharField(label='Kohteen nimi', max_length='200')
    start_date = forms.DateField(label='Aloitus pvm', widget=forms.SelectDateWidget(empty_label="Nothing", years=constants.YEARS))
    end_date = forms.DateField(label='Lopetus pvm', widget=forms.SelectDateWidget(empty_label="Nothing", years=constants.YEARS))
    destination_type = forms.CharField(label='Rakennustyyppi', widget=forms.Select(choices=constants.DESTINATION_TYPES, attrs={'cols': 50}))
    building_material = forms.CharField(label='Rakennusmateriaali', widget=forms.Select(choices=constants.BUILDING_MATERIALS))
    service = forms.CharField(label='Palvelu', widget=forms.Select(choices=constants.SERVICES))
    construction_operation = forms.CharField(label='Rakennustoimenpide', widget=forms.Select(choices=constants.CONSTRUCTION_OPERATIONS))
    specific_project_type = forms.CharField(label='Osaamisalue', max_length='200')
    project_description = forms.CharField(label='Projektin kuvaus', max_length='500', widget=forms.Textarea(attrs={'cols': 50, 'rows': 5}))
    documentation_path = forms.CharField(label='Polku tiedostojen sijaintiin', max_length='200')
    project_manager = forms.CharField(label='Projektin johtaja', max_length='100')