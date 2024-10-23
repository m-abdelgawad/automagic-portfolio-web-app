import logging
from django.urls import reverse
from django.test import TestCase


logging.disable(logging.CRITICAL)


class ViewsTestCase(TestCase):
    def test_index_loads_properly(self):
        # Now the client should be authenticated as the superuser
        response = self.client.get(reverse('home:home'))

        # Check if the response status code is 200
        self.assertEqual(response.status_code, 200)
