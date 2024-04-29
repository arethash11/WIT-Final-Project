from django.contrib import admin
from .models import Category, Customer, Product, Order



admin.site.register(Category)


class CustomerAdmin(admin.ModelAdmin):
    list_display = ("last_name", "first_name", "phone", "email")

admin.site.register(Customer, CustomerAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "price", "is_sale", "sale_price", "category")

admin.site.register(Product, ProductAdmin)


class OrderAdmin(admin.ModelAdmin):
    list_display = ("date", "product", "quantity", "customer", "address", "phone", "status")

admin.site.register(Order, OrderAdmin)

