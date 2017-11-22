from django.conf.urls import url
from .views import RestaurantLocationListView

app_name = 'restaurants'

urlpatterns = [
    url(r'^$', RestaurantLocationListView.as_view(), name='restaurant_list'),
]
