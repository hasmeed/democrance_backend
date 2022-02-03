# from audioop import reverse
# from http import client
# from django.test import client
from rest_framework import status
import json
from django.test import TestCase, Client
from rest_framework.test import APITestCase
from django.urls import reverse_lazy

class CustomerTestCases(TestCase):

    def setUp(self):
        self.client = Client()
        self.valid_customer_payload = {
            'first_name': 'Mufin',
            'last_name': 'Pamerion',
            "dob": "2008-02-20"
        }

    def test_create_customer(self):
        response = self.client.post(
            '/api/v1/customer/create_customer',
            data = json.dumps(self.valid_customer_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)