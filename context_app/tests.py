from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework.test import APIRequestFactory

from . import views

# Create your tests here.
# Code to test all api functionality
class TestAgileValues(APITestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.view = views.AgileValuesViewset.as_view()
        self.uri = '/api/agile_values/'

    def test_list(self):
        request = self.factory.get(self.uri)
        response = self.view(request)
        self.assertEqual(
            response.status_code, 200,
            'Expected Response Code 200, received {0} instead.'.
            format(response.status_code)
        )
    
    def test_create(self):
        params = {
            "heading":"Agile value test",
            "definition":"Agile value definition test"
        }
        response = self.client.post(self.uri, params)
        self.assertEqual(
            response.status_code, 201,
            'Expected Response Code 201, received {0} instead.'.
            format(response.status_code)
            )


class TestAgilePrincipleViewset(APITestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.view = views.AgilePrincipleViewset.as_view()
        self.uri = '/api/agile_principles/'

    def test_list(self):
        request = self.factory.get(self.uri)
        response = self.view(request)
        self.assertEqual(
            response.status_code, 200,
            'Expected Response Code 200, received {0} instead.'.
            format(response.status_code)
        )
    
    def test_create(self):
        params = {
            "heading":"Agile Principles test",
            "definition":"Agile Principles definition test"
        }
        response = self.client.post(self.uri, params)
        self.assertEqual(
            response.status_code, 201,
            'Expected Response Code 201, received {0} instead.'.
            format(response.status_code))

