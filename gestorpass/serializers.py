# Este archivo serializer.py hemos de crearlo nosotros mismos.
from rest_framework import serializers
from .models import PasswordEntry

class PasswordEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = PasswordEntry
        fields = '__all__'


