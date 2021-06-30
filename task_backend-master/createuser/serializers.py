from .models import userprofile
from rest_framework import serializers
class UpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = userprofile
        fields = '__all__'