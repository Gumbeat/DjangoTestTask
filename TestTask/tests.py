from django.test import TestCase, Client
from django.urls import reverse

from TestTask.models import Product, Organization, District, Network, Category
import json


class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.product_list_url = reverse('products')
        self.product_detail_url = reverse('product_detail', args=['1'])
        self.organization_list_url = reverse('organizations')
        self.organization_detail_url = reverse('organization_detail', args=['1'])
        self.organization_by_district_url = reverse('organizations_by_district', args=['1'])

    def test_product_list(self):
        response = self.client.get(self.product_list_url)
        self.assertEqual(response.status_code, 200)

    def test_product_detail(self):
        response = self.client.get(self.product_detail_url)
        self.assertEqual(response.status_code, 200)

    def test_organization_list(self):
        response = self.client.get(self.organization_list_url)
        self.assertEqual(response.status_code, 200)

    def test_organization_detail(self):
        response = self.client.get(self.organization_detail_url)
        self.assertEqual(response.status_code, 200)

    def test_organization_by_district(self):
        response = self.client.get(self.organization_by_district_url)
        self.assertEqual(response.status_code, 200)
