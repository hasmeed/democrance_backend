from rest_framework import status
import json
from django.test import TestCase, Client
from customer.test.CustomerFactory import CustomerFactory


class PolicyTestCases(TestCase):

    def setUp(self):
        self.client = Client()
        self.customer = CustomerFactory()

        self.valid_quote_payload = {
            "customer_id":self.customer.id,
            "type":"personal-accident"
            }

    def test_new_quote_policy(self):
        response = self.client.post(
            '/api/v1/policy/quote',
            data = json.dumps(self.valid_quote_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
