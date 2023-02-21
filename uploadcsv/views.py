import codecs
import csv

from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Product
from .serializers import ProductSerializer, ProfileSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework import status



class ProductImportCSV(APIView):
    """
    A simple Upload Product As CSV.
    """
    permission_classes = [IsAuthenticated]
    serializer_class = ProductSerializer

    def post(self, request, format=None):
        """Upload data from CSV, with validation."""
        file = request.FILES.get("file")
        if not file:
            return Response({"msg":"file not attached"}, status = status.HTTP_404_NOT_FOUND)
        reader = csv.DictReader(codecs.iterdecode(file, "utf-8"), delimiter=",")
        data = list(reader)

        serializer = self.serializer_class(data=data, many=True)
        if serializer.is_valid(raise_exception=True):

            product_list = []
            for row in serializer.data:
                product_list.append(
                    Product(
                        user_id=row["user"],
                        category=row["category"],
                        price=row["price"],
                        name=row["name"],
                        description=row["description"],
                        quantity=row["quantity"],
                    )
                )

            Product.objects.bulk_create(product_list)

            return Response("Successfully upload the data")
        return Response(serializer.errors)


class ProfileUploadCSV(APIView):
  def post(self, request, format=None):
    serializer = ProfileSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response({'msg':'Resume Uploaded Successfully', 'status':'success', 'candidate':serializer.data}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors)