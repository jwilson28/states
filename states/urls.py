from django.urls import path

from . import views

app_name = 'states'
urlpatterns = [
    path('', views.index, name='index'),
    path('cities/', views.city_list, name = 'city_list'),
    path('state/<int:state_id>/', views.state_detail, name='state_detail'),
    path('city/<int:city_id>/', views.city_detail, name='city_detail'),
]