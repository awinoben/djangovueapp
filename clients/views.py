from django.shortcuts import render

from clients.models import Client
from clients.serializers import ClientSerializer
from rest_framework import generics
from rest_framework.decorators import api_view
from django.http import HttpResponse


class ClientList(generics.ListCreateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

class ClientDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer