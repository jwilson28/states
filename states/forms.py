from django.forms import ModelForm
from .models import State, City


class StateForm(ModelForm):
    class Meta:
        model = State
        fields = ['name', 'abbrev', 'population']


class CityForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super(CityForm, self).__init__(*args, **kwargs)
        instance = getattr(self, 'instance', None)
        if instance and instance.pk:
            self.fields['state'].disabled = True

    class Meta:
        model = City
        fields = ['name', 'abbrev', 'population', 'state']