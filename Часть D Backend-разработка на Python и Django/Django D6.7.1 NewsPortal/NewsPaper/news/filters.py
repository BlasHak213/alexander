from django_filters import FilterSet, DateTimeFilter, ModelChoiceFilter
from django.forms import DateTimeInput
from .models import Post, Category
from django import forms
from django.core.exceptions import ValidationError


class PostFilter(FilterSet):
    dateCreation_after = DateTimeFilter(
        label='Post added after',
        field_name='dateCreation',
        lookup_expr='gt',
        widget=DateTimeInput(
            format='%Y-%m-%dT%H:%M',
            attrs={'type': 'datetime-local'},
        )
    )
    category_choice = ModelChoiceFilter(
        label='Post Category',
        field_name='postcategory__categoryThrough',
        queryset=Category.objects.all(),
        empty_label='Все',
    )

    class Meta:
        model = Post
        fields = {
            # 'postcategory__categoryThrough': ['exact'],
            # 'postCategory': ['exact'],
            'title': ['icontains'],
            'categoryType': ['exact'],
        }
