from rest_framework import serializers
from .models import Client


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ('first_name', 'last_name', 'other_names', 'filled','id_number','phone_number',
        'race','gender','dob','occupation','income','education', 'created_at', 'updated_at'
        )