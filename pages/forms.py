from django import forms

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