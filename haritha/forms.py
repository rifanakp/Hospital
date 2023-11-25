from django import forms
from . models import Booking
class DateInput(forms.DateInput):
    input_type='date'
class BookingForm(forms.ModelForm):
    class Meta:
        model=Booking
        fields='__all__'
        widgets = {
            'booked_to':DateInput()
        }
        labels = {
            'p_name':'Name',
            'p_phone':'Phone',
            'dco_name':'Doctor Name',
        }