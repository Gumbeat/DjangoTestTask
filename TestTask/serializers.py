from rest_framework import serializers
from TestTask.models import Category, District, Network, Organization, Product, ProductPrice


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class DistrictSerializer(serializers.ModelSerializer):
    class Meta:
        model = District
        fields = '__all__'


class NetworkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Network
        fields = '__all__'


class OrganizationProductPriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductPrice
        fields = ['product', 'price']
        depth = 2


class ProductPriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductPrice
        fields = ['organization', 'price']
        depth = 2


class OrganizationSerializer(serializers.ModelSerializer):
    products = OrganizationProductPriceSerializer(many=True, source='product_price')
    districts = DistrictSerializer(many=True, read_only=True)

    class Meta:
        depth = 1
        model = Organization
        fields = ['id', 'description', 'products', 'districts', 'network']


class ProductSerializer(serializers.ModelSerializer):
    organizations = ProductPriceSerializer(many=True, source='product_price')

    class Meta:
        model = Product
        fields = ['id', 'name', 'category', 'organizations']

