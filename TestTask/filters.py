import django_filters
from TestTask.models import Organization


class OrganizationFilter(django_filters.FilterSet):
    price_gte = django_filters.NumberFilter(field_name='product_price__price', lookup_expr='gte')
    price_lte = django_filters.NumberFilter(field_name='product_price__price', lookup_expr='lte')
    product_name = django_filters.CharFilter(field_name='product_price__product__name', lookup_expr='icontains')
    category = django_filters.CharFilter(field_name='product_price__product__category__name', lookup_expr='icontains')

    class Meta:
        model = Organization
        fields = {
            'product_name',
            'category',
            'price_gte',
            'price_lte',
        }
