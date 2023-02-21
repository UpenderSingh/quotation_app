from rest_framework import serializers
from quotationapp.models import Item

class ItemSearchSerializer(serializers.ModelSerializer):
  class Meta:
    model = Item
    fields = '__all__'