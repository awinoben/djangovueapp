from django.test import TestCase
from clients.models import Client
# Create your tests here.

class ClientTestCase(TestCase):
    def setUp(self):
        Client.objects.create(first_name="John", last_name="Njoroge", other_names="Maina",filled="null",id_number="1234567", phone_number="0706877851",race="Kenyan",gender="Male",dob="1991-10-23",occupation="Software", income="1234566",education="University")
        Client.objects.create(first_name="Wendy", last_name="Wayua", other_names="Kimani",filled="null",id_number="1234567", phone_number="0706877851",race="Kenyan",gender="Female",dob="1991-10-23",occupation="Finance", income="1234566",education="University")

    def test_client_gender(self):
        client_john = Client.objects.get(first_name='John')
        client_wendy = Client.objects.get(first_name='Wendy')
        self.assertEqual(
            client_john.get_gender(), "John is a male.")
        self.assertEqual(
            client_wendy.get_gender(), "Wendy is a female.")