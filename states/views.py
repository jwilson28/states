from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import State, City
from .forms import StateForm, CityForm


def index(request):
    states = State.objects.all()
    if request.method == 'POST':
        state_form = StateForm(request.POST)
        if state_form.is_valid():
            state_form.save()
            state_form = StateForm()
            return render(request, 'states/templates/index.html', {'states':states, 'state_form':state_form})
    state_form = StateForm()
    return render(request, 'states/templates/index.html', {'states': states, 'state_form': state_form})

def city_list(request):
    cities = City.objects.all().order_by('-name')
    if request.method == 'POST':
        city_form = CityForm(request.POST)
        if city_form.is_valid():
            city_form.save()
            city_form = CityForm()
            return render(request, 'states/templates/city_list.html', {'cities': cities, 'city_form':city_form})
    city_form = CityForm()
    return render(request, 'states/templates/city_list.html', {'cities': cities, 'city_form':city_form})


def state_detail(request, state_id):
    instance = get_object_or_404(State, pk=state_id)
    edit_state_form = StateForm(request.POST or None, instance=instance)
    context = {
        'state':instance,
        'edit_state_form':edit_state_form,
    }
    if edit_state_form.is_valid():
        edit_state_form.save()
    return render(request, 'states/templates/state_detail.html', context)

def city_detail(request, city_id):
    city = get_object_or_404(City, pk=city_id)
    edit_city_form = CityForm(request.POST or None, instance=city)
    context = {
        'city':city,
        'edit_city_form':edit_city_form,
    }
    if edit_city_form.is_valid():
        edit_city_form.save()
    return render(request, 'states/templates/city_detail.html', context)
