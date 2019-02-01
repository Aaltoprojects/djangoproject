from django import forms

class NameForm(forms.Form):
    coname = forms.CharField(label='Company name', max_length=100)
    coid = forms.CharField(label='Company ID', max_length=100)

class create_employee_form(forms.Form):
    fname = forms.CharField(label='First name', max_length=100)
    surname = forms.CharField(label='Surname', max_length=100)
    title = forms.CharField(label='Title', max_length=100)
    function = forms.CharField(label='Function', max_length=100)

class search_employee_form(forms.Form):
	function = forms.CharField(label='Employee function', max_length=100)