from django.contrib import admin
from .models import Category, Product, Material


class ProductAdmin(admin.ModelAdmin):
    # list_display — это список или кортеж со всеми полями, которые вы хотите видеть в таблице с товарами
    list_display = [field.name for field in Product._meta.get_fields()]  # генерируем список имён всех полей для более красивого отображения

    def product_material(self, product):
        return ', '.join([material.name for material in product.material.all()])

    list_display = ('id', 'name', 'description', 'quantity', 'category', 'price', 'product_material')

admin.site.register(Category)
admin.site.register(Product, ProductAdmin)
admin.site.register(Material)