import json
from rest_framework import status
from django.test import TestCase, Client
from django.urls import reverse
from ..models import Client
from ..serializers import ClientSerializer


# initialize the APIClient app
client = Client()


class GetAllClientsTest(TestCase):
    """ Test module for GET all patients API """

    def setUp(self):
        Client.objects.create(first_name="John", last_name="Njoroge", other_names="Maina",filled="null",id_number="1234567", phone_number="0706877851",race="Kenyan",gender="Male",dob="1991-10-23",occupation="Software", income="1234566",education="University")
        Client.objects.create(first_name="Wendy", last_name="Wayua", other_names="Kimani",filled="null",id_number="1234567", phone_number="0706877851",race="Kenyan",gender="Female",dob="1991-10-23",occupation="Finance", income="1234566",education="University")

    def test_get_all_clients(self):
        # get API response
        response = client.get(reverse('get_post_experiments'))
        # get data from db
        clients = Client.objects.all()
        serializer = ClientSerializer(clients, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

class GetSinglePatientTest(TestCase):
    """ Test module for GET single patient API """

    def setUp(self):
        self.patient = Client.objects.create(first_name="John", last_name="Njoroge", other_names="Maina",filled="null",id_number="1234567", phone_number="0706877851",race="Kenyan",gender="Male",dob="1991-10-23",occupation="Software", income="1234566",education="University")

        self.patient2 = Client.objects.create(first_name="John", last_name="Njoroge", other_names="Maina",filled="null",id_number="1234567", phone_number="0706877851",race="Kenyan",gender="Male",dob="1991-10-23",occupation="Software", income="1234566",education="University")

    def test_get_valid_single_client(self):
        response = client.get(
            reverse('get_delete_update_client', kwargs={'pk': self.patient2.pk}))
        client = Client.objects.get(pk=self.patient2.pk)
        serializer = ClientSerializer(client)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_invalid_single_client(self):
        response = client.get(
            reverse('get_delete_update_client', kwargs={'pk': 30}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

class CreateNewExperimentTest(TestCase):
    """ Test module for inserting a new patient """

    def setUp(self):
        self.valid_payload = {
           'first_name': 'papa',
            'last_name': 'ben',
            'other_names': 'kabila',
            'filled': 'null',
            'id_number': '1234567',
            'phone_number': '0706877851',
            'race': 'Kenyan',
            'gender': 'Male',
            'dob': '1991-10-23',
            'occupation': 'Software',
            'income': '1234566',
            'education': 'University',

        }
        self.invalid_payload = {
            'first_name': '',
            'last_name': 'robben',
            'other_names': 'nasty',
            'filled': 'null',
            'id_number': '1234567',
            'phone_number': '0706877851',
            'race': 'Kenyan',
            'gender': 'Male',
            'dob': '1991-10-23',
            'occupation': 'Dev',
            'income': '1234566',
            'education': 'University',
        }

    def test_create_valid_client(self):
        response = client.post(
            reverse('get_post_clients'),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid_client(self):
        response = client.post(
            reverse('get_post_clients'),
            data=json.dumps(self.invalid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

class UpdateSingleClientTest(TestCase):
    """ Test module for updating an existing experiment record """

    def setUp(self):
        self.patient = Client.objects.create(first_name="John", last_name="Njoroge", other_names="Maina",filled="null",id_number="1234567", phone_number="0706877851",race="Kenyan",gender="Male",dob="1991-10-23",occupation="Software", income="1234566",education="University")

        self.patient2 = Client.objects.create(first_name="John", last_name="Njoroge", other_names="Maina",filled="null",id_number="1234567", phone_number="0706877851",race="Kenyan",gender="Male",dob="1991-10-23",occupation="Software", income="1234566",education="University")
        self.valid_payload = {
            'first_name': 'papa',
            'last_name': 'ben',
            'other_names': 'kabila',
            'filled': 'null',
            'id_number': '1234567',
            'phone_number': '0706877851',
            'race': 'Kenyan',
            'gender': 'Male',
            'dob': '1991-10-23',
            'occupation': 'Software',
            'income': '1234566',
            'education': 'University'
        }
        self.invalid_payload = {
            'first_name': '',
            'last_name': 'robben',
            'other_names': 'nasty',
            'filled': 'null',
            'id_number': '1234567',
            'phone_number': '0706877851',
            'race': 'Kenyan',
            'gender': 'Male',
            'dob': '1991-10-23',
            'occupation': 'Dev',
            'income': '1234566',
            'education': 'University'
        }

    def test_valid_update_client(self):
        response = client.put(
            reverse('get_delete_update_client', kwargs={'pk': self.patient2.pk}),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_invalid_update_client(self):
        response = client.put(
            reverse('get_delete_update_client', kwargs={'pk': self.patient2.pk}),
            data=json.dumps(self.invalid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

class DeleteSingleClientTest(TestCase):
    """ Test module for deleting an existing patient record """

    def setUp(self):
        self.patient = Client.objects.create(first_name="John", last_name="Njoroge", other_names="Maina",filled="null",id_number="1234567", phone_number="0706877851",race="Kenyan",gender="Male",dob="1991-10-23",occupation="Software", income="1234566",education="University")

        self.patient2 = Client.objects.create(first_name="John", last_name="Njoroge", other_names="Maina",filled="null",id_number="1234567", phone_number="0706877851",race="Kenyan",gender="Male",dob="1991-10-23",occupation="Software", income="1234566",education="University")

    def test_valid_delete_client(self):
        response = client.delete(
            reverse('get_delete_update_client', kwargs={'pk': self.patient2.pk}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_invalid_delete_patient(self):
        response = client.delete(
            reverse('get_delete_update_client', kwargs={'pk': 30}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
