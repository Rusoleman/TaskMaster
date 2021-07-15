from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from members.models import Member


class MembersSerializer(ModelSerializer):

    def validate(self, attrs):
        if '{' in attrs['first_name']:
            raise serializers.ValidationError('Nombe no valido')
        return attrs
    class Meta:
        model = Member
        fields = ("first_name", "last_name", "email", "password")