from django.contrib import admin
from .models import Category, Ad, AdResponse


admin.site.register(Category)
admin.site.register(Ad)
admin.site.register(AdResponse)
