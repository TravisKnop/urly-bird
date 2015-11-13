
from rest_framework import serializers
from api.models import UrlRecord, Profile


class UrlSerializer(serializers.ModelSerializer):
    class Meta:
        model = UrlRecord
        field = ('long_url', 'short_url')


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        lookup_field = 'user'
