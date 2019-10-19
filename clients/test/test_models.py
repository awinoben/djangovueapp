from django.test import TestCase
from clients.models import Client


class ClientTest(TestCase):
    """ Test module for Clients model """

    def setUp(self):
       self.patient = Client.objects.create(first_name="John", last_name="Njoroge", other_names="Maina",filled="null",id_number="1234567", phone_number="0706877851",race="Kenyan",gender="Male",dob="1991-10-23",occupation="Software", income="1234566",education="University")

       self.patient2 = Client.objects.create(first_name="Papa", last_name="Nasty", other_names="Maina",filled="null",id_number="1234567", phone_number="0706877851",race="Kenyan",gender="Male",dob="1991-10-23",occupation="Software", income="1234566",education="University")

    def test_experiment_email(self):
        client_record = Client.objects.get(first_name='John')
        client_record2 = Client.objects.get(first_name='Papa')
        self.assertEqual(
            client_record.get_phone(), "Record belongs to 0706877851.")
        self.assertEqual(
            client_record2.get_phone(), "Record 2 belongs to 0706877851.")