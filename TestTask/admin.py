from django.contrib import admin
from .models import District, Product, Organization, Network, ProductPrice, Category

# Register your models here.
admin.site.register(District)
admin.site.register(Category)
admin.site.register(Network)
admin.site.register(Organization)
admin.site.register(Product)
admin.site.register(ProductPrice)
