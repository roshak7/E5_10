from django.urls import path
from cars.views import CarList


app_name = 'cars'
urlpatterns = [
    path('', CarList.as_view(), name='car-list'), ]
