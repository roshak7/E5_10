from django.shortcuts import render
from django.db.models import Q
from django.views.generic import ListView

from cars.models import Car, Color


class CarList(ListView):
    model = Car
    template_name = 'index.html'
    context_object_name = 'cars'
    queryset = Car.objects.select_related('color').all()
    # ordering = ['manufacturer', 'model']

    def get_context_data(self, **kwargs):
        context = super(CarList, self).get_context_data(**kwargs)

        models = self.queryset.values('manufacturer', 'model').distinct()
        context['models'] = models

        manufacturers = set([model['manufacturer'] for model in models])
        context['manufacturers'] = sorted(manufacturers)

        colors = Color.objects.all()
        context['colors'] = colors
        return context

    def get_queryset(self):
        filters = self.get_filters()
        return super().get_queryset().filter(*filters)

    def get_filters(self):
        filters = []
        search_manufacturer = self.request.GET.get('car-manufacturer')
        search_model = self.request.GET.get('car-model')
        search_color = self.request.GET.get('car-color')
        search_transmission = self.request.GET.get('car-transmission')
        year_min = self.request.GET.get('year-min')
        year_max = self.request.GET.get('year-max')

        if search_model:
            search_model, search_manufacturer = search_model.split(' | ')
            filters.append(Q(model=search_model))
        if search_manufacturer:
            filters.append(Q(manufacturer=search_manufacturer))
        if search_color:
            filters.append(Q(color=search_color))
        if search_transmission:
            filters.append(Q(transmission=search_transmission))
        if year_min:
            filters.append(Q(year__gte=year_min))
        if year_max:
            filters.append(Q(year__lte=year_max))

        return filters
