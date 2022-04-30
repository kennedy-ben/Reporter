from dataclasses import field
from rest_framework import serializers
from .models import Drinks 

class DrinkSerializer(serializers.ModelSerializer):
    class Meta:
        modal= Drinks
        field = ['id', 'name', 'description']
