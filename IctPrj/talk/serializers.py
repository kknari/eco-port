from rest_framework import serializers
from .models import talk

class talkSerializer(serializers.ModelSerializer):
    class Meta:
        model = talk
        fields = '__all__'