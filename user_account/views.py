from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.contrib.auth import authenticate
from user_account.serializers import (
  UserRegistrationSerializer, UserLoginSerializer,
  UserProfileSerializer, CustomerSearchSerializer)
from user_account.renderers import UserRenderer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
from django.views.generic import View, TemplateView
from rest_framework import generics
from rest_framework.filters import SearchFilter
from user_account.models import User


# Generate Token Manually
def get_tokens_for_user(user):
  refresh = RefreshToken.for_user(user)
  return {
      'refresh': str(refresh),
      'access': str(refresh.access_token),
  }


class UserRegistrationView(APIView):
  renderer_classes = [UserRenderer]
  def post(self, request, format=None):
    serializer = UserRegistrationSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()
        token = get_tokens_for_user(user)
        return Response({"token": token, 'msg':'Registration Successful'}, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserLoginView(APIView):
  def post(self, request, format=None):
    serializer = UserLoginSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        email = serializer.data.get("email")
        password = serializer.data.get("password")
        user = authenticate(email=email, password=password)
        if user is not None:
          token = get_tokens_for_user(user)
          return Response({"token":token, "msg":"Login Success"}, status=status.HTTP_200_OK)
        else:
          return Response({"errors":{"non_field_errors":["Email or Password is not Valid"]}}, status=status.HTTP_404_NOT_FOUND)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserProfileView(APIView):
  renderer_classes = [UserRenderer]
  permission_classes = [IsAuthenticated]
  def get(self, request, format=None):
    serializer = UserProfileSerializer(request.user)
    return Response(serializer.data, status=status.HTTP_200_OK)


class LoginPageView(View):
    template_name = 'user_account/dashboardpage.html'
    
    def get(self, request):
        #form = self.form_class()
        message = ''
        return render(request, self.template_name, context={'message': message})


class CustomerSearchView(generics.ListAPIView):
   queryset = User.objects.all()
   serializer_class = CustomerSearchSerializer
   filter_backends = [SearchFilter]
   search_fields = ['id', 'name', 'email'] 