from django import forms
from carapp.models import cars

class car_form(forms.ModelForm):
    class Meta:
        model = cars
        fields = '__all__'