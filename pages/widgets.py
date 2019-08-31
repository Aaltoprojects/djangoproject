from django.forms import DateInput

class FengyuanChenDatePickerInput(DateInput):
    template_name = 'fengyuanchen_datepicker.html'