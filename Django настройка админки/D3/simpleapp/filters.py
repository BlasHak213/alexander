from django_filters import FilterSet, ModelChoiceFilter
from .models import Product, Material


class ProductFilter(FilterSet):
    material = ModelChoiceFilter(
        label='Material',
        field_name='productmaterial__material',
        queryset=Material.objects.all(),
        empty_label='Все',
    )

    class Meta:
        model = Product
        fields = {
            'name': ['icontains'],
            'quantity': ['gt'],
            'price': ['lt', 'gt', ],
        }
