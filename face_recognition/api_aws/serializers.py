from .models import Face 
from django.contrib.auth.models import User 
from rest_framework import serializers


class FaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Face
        fields = '__all__'
        