from django.test import TestCase, Client
from django.urls import reverse

from TestTask.models import Product, Organization, District, Network, Category, ProductPrice
import json


class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.product_list_url = reverse('products')
        self.product_detail_url = reverse('product_detail', args=['1'])
        self.organization_list_url = reverse('organizations')
        self.organization_detail_url = reverse('organization_detail', args=['1'])
        self.organization_by_district_url = reverse('organizations_by_district', args=['1'])

        self.product_name_filter = 'product_name='
        self.category_filter = 'category='
        self.price_gte_filter = 'price_gte='
        self.price_lte_filter = 'price_lte='

        self.district_1 = District.objects.create(name='Ворошиловский')
        self.district_2 = District.objects.create(name='Киевский')

        self.network1 = Network.objects.create(name='Продуктовый магазин')
        self.network2 = Network.objects.create(name='Магазин одежды')

        self.category1 = Category.objects.create(name='Еда')
        self.category2 = Category.objects.create(name='Одежда')

        self.product1 = Product.objects.create(name='Fanta', category_id=1)
        self.product2 = Product.objects.create(name='CocaCola', category_id=1)
        self.product3 = Product.objects.create(name='Jacket', category_id=2)
        self.product4 = Product.objects.create(name='Shirt', category_id=2)

        self.organization1 = Organization.objects.create(network_id=1, description='Описание 1')
        self.organization1.districts.add(self.district_1)
        self.organization2 = Organization.objects.create(network_id=1, description='Описание 2')
        self.organization2.districts.add(self.district_2)
        self.organization3 = Organization.objects.create(network_id=2, description='Описание 3')
        self.organization3.districts.add(self.district_1)
        self.organization4 = Organization.objects.create(network_id=2, description='Описание 4')
        self.organization4.districts.add(self.district_2)

        self.product_price1 = ProductPrice.objects.create(product_id=1, organization_id=1, price=15)
        self.product_price2 = ProductPrice.objects.create(product_id=1, organization_id=2, price=14)
        self.product_price3 = ProductPrice.objects.create(product_id=2, organization_id=1, price=16)
        self.product_price4 = ProductPrice.objects.create(product_id=2, organization_id=2, price=17)

        self.product_price5 = ProductPrice.objects.create(product_id=3, organization_id=3, price=10000)
        self.product_price6 = ProductPrice.objects.create(product_id=3, organization_id=4, price=9000)
        self.product_price7 = ProductPrice.objects.create(product_id=4, organization_id=3, price=5000)
        self.product_price8 = ProductPrice.objects.create(product_id=4, organization_id=4, price=4500)

    def test_product_list(self):
        response = self.client.get(self.product_list_url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 4)

    def test_product_detail(self):
        response = self.client.get(self.product_detail_url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data['organizations']), 2)
        self.assertEqual(response.data['name'], 'Fanta')

    def test_organization_list(self):
        response = self.client.get(self.organization_list_url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 4)

    def test_organization_detail(self):
        response = self.client.get(self.organization_detail_url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data['products']), 2)
        self.assertEqual(response.data['description'], 'Описание 1')

    def test_organization_by_district(self):
        response = self.client.get(self.organization_by_district_url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 2)
        self.assertEqual(response.data[0]['network']['name'], 'Продуктовый магазин')

    def test_name_filter(self):
        response = self.client.get(f'{self.organization_by_district_url}?{self.product_name_filter}Fanta')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data[0]['products'][0]['product']['name'], 'Fanta')
        self.assertEqual(len(response.data), 1)

    def test_category_filter(self):
        response = self.client.get(f'{self.organization_by_district_url}?{self.category_filter}2')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data[0]['products'][0]['product']['category']['id'], 2)
        self.assertEqual(len(response.data), 1)

    def test_price_gte_filter(self):
        response = self.client.get(f'{self.organization_by_district_url}?{self.price_gte_filter}500')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(float(response.data[0]['products'][0]['price']), 10000.0)
        self.assertEqual(len(response.data), 1)

    def test_price_lte_filter(self):
        response = self.client.get(f'{self.organization_by_district_url}?{self.price_lte_filter}500')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(float(response.data[0]['products'][0]['price']), 15.0)
        self.assertEqual(len(response.data), 1)
