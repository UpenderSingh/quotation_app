from rest_framework import serializers
from uploadcsv.models import Product, Profile


# Serializer
class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = "__all__"


class ProfileSerializer(serializers.ModelSerializer):
  class Meta:
    model=Profile
    fields = ['id', 'name', 'state', 'gender', 'location', 'csf_file']