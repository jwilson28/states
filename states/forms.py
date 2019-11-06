from django.forms import ModelForm
from .models import State, City


class StateForm(ModelForm):
    class Meta:
        model = State
        fields = ['name', 'abbrev', 'population']


class CityForm(ModelForm):
    class Meta:
        model = City
        fields = ['name', 'abbrev', 'population', 'state']