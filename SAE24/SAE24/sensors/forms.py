from django import forms
from .models import Sensor

class SensorForm(forms.ModelForm):
    class Meta:
        model = Sensor
        fields = ['room', 'location']

class SensorDataFilterForm(forms.Form):
    start_date = forms.DateField(required=False, widget=forms.DateInput(attrs={'type': 'date'}))
    end_date = forms.DateField(required=False, widget=forms.DateInput(attrs={'type': 'date'}))
    min_temperature = forms.DecimalField(required=False, decimal_places=2, max_digits=5)
    max_temperature = forms.DecimalField(required=False, decimal_places=2, max_digits=5)