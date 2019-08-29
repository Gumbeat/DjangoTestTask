from django.test import TestCase, Client
from django.urls import reverse
from rest_framework.test import APITestCase

from TestTask.models import Product, Organization
import json


class TestViews(APITestCase):

    def setUp(self):
        self.client = Client()
        self.product_list_url = reverse('products')
        self.product_detail_url = reverse('product', args=['1'])
        self.organization_list_url = reverse('organizations')
        self.organization_detail_url = reverse('organization', args=['1'])
        self.organization_by_district_url = reverse('organizations', args=['1'])

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
