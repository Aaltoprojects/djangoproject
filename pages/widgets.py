from django.forms import DateInput

class FengyuanChenDatePickerInput(DateInput):
    template_name = 'snippets/fengyuanchen_datepicker.html'