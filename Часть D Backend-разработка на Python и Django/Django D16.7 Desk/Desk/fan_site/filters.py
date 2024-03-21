import django_filters
from django_filters import FilterSet
from .models import AdResponse, Ad


class AdFilter(FilterSet):
    ad = django_filters.ModelChoiceFilter(empty_label="Все объявления", label="Объявления:")

    class Meta:
        model = AdResponse
        fields = ['ad']

    def __init__(self, *args, **kwargs):
        super(AdFilter, self).__init__(*args, **kwargs)
        self.filters['ad'].queryset = Ad.objects.filter(user_id=kwargs['request'])

