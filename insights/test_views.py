import logging

from django.test import TestCase
from django.urls import reverse

logging.disable(logging.CRITICAL)


class ViewsTestCase(TestCase):
    def test_index_loads_properly(self):
        # Now the client should be authenticated as the superuser
        response = self.client.get(reverse('insights:insights_home'))

        # Check if the response status code is 200
        self.assertEqual(response.status_code, 200)
