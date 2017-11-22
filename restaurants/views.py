from django.shortcuts import render
from django.views.generic import ListView
from restaurants.models import RestaurantLocation

class RestaurantLocationListView(ListView):
    model = RestaurantLocation
    context_object_name = 'restaurants'
    template_name = 'restaurants/restaurant_list.html'

    def get_queryset(self):
        return RestaurantLocation.objects.order_by('name')
