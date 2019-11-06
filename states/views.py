from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import State, City
from .forms import StateForm, CityForm


def index(request):
    if request.method == 'POST':
        state_form = StateForm(request.POST)
        if state_form.is_valid():
            state_form.save()
            states = State.objects.all()
            return render(request, 'states/templates/index.html', {'states':states, 'state_form':state_form})
    states = State.objects.all()
    state_form = StateForm()
    return render(request, 'states/templates/index.html', {'states': states, 'state_form': state_form})

def city_list(request):
    cities = City.objects.all().order_by('-name')
    if request.method == 'POST':
        city_form = CityForm(request.POST)
        if city_form.is_valid():
            city_form.save()
            return render(request, 'states/templates/city_list.html', {'cities': cities, 'city_form':city_form})
    city_form = CityForm()
    return render(request, 'states/templates/city_list.html', {'cities': cities, 'city_form':city_form})


def state_detail(request, state_id):
    state = get_object_or_404(State, pk=state_id)
    return render(request, 'states/templates/state_detail.html', {'state':state})

def city_detail(request, city_id):
    city = get_object_or_404(City, pk=city_id)
    return render(request, 'states/templates/city_detail.html', {'city':city})
