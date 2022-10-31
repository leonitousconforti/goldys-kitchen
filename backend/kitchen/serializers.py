# from attr import field
from rest_framework import serializers
from .models import *

class IngredientsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = ('id', 'name')

# class RecepieSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Recepie
#         fields = ('id', 'name', 'ingredients')
#
# class QuantitySerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Quantity
#         fields = ('id', 'recepie', 'ingredient', 'quantity')
