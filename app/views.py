

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics

from app.serializer import AlergenSerializer, CreateYourOwnSerializer, DrinkSerializer, FeaturedGameSerializer, PancakeSerializer
from .models import Alergen, Pancake, CreateYourOwn, Drink, FeaturedGame

class AlergenListCreateView(APIView):
    def get(self, request, *args, **kwargs):
        alergens = Alergen.objects.all()
        serializer = AlergenSerializer(alergens, many=True)
        return Response(serializer.data)

class PancakeListCreateView(APIView):
    def get(self, request, *args, **kwargs):
        pancakes = Pancake.objects.all()
        serializer = PancakeSerializer(pancakes, many=True)
        return Response(serializer.data)

class CreateYourOwnListCreateView(APIView):
    def get(self, request, *args, **kwargs):
        create_your_own_items = CreateYourOwn.objects.all()
        serializer = CreateYourOwnSerializer(create_your_own_items, many=True)
        return Response(serializer.data)

class DrinkListCreateView(APIView):
    def get(self, request, *args, **kwargs):
        drinks = Drink.objects.all()
        serializer = DrinkSerializer(drinks, many=True)
        return Response(serializer.data)

class FeaturedGameListCreateView(APIView):
    def get(self, request, *args, **kwargs):
        featured_games = FeaturedGame.objects.all()
        serializer = FeaturedGameSerializer(featured_games, many=True)
        return Response(serializer.data)
