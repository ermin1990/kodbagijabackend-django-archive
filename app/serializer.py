# serializers.py
from rest_framework import serializers
from .models import Alergen, Pancake, CreateYourOwn, Drink, FeaturedGame

class AlergenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alergen
        fields = '__all__'

class PancakeSerializer(serializers.ModelSerializer):
    alergens = AlergenSerializer(many=True, read_only=True)
    class Meta:
        model = Pancake
        fields = '__all__'

class CreateYourOwnSerializer(serializers.ModelSerializer):
    alergens = AlergenSerializer(many=True, read_only=True)
    class Meta:
        model = CreateYourOwn
        fields = '__all__'

class DrinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Drink
        fields = '__all__'

class FeaturedGameSerializer(serializers.ModelSerializer):
    class Meta:
        model = FeaturedGame
        fields = '__all__'
