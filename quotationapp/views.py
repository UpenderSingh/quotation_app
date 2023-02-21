from django.shortcuts import render
from .serializers import ItemSearchSerializer
from .models import Item
from rest_framework.filters import SearchFilter
from rest_framework import generics

# Create your views here.
class ItemSearchView(generics.ListAPIView):
   queryset = Item.objects.all()
   serializer_class = ItemSearchSerializer
   filter_backends = [SearchFilter]
   search_fields = ['name'] 