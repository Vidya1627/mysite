from django.shortcuts import render

from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from .models import Company, User, Product
from .serializers import CompanySerializer, UserSerializer, ProductSerializer

class CompanyView(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer


class UserView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    def update(self, request, pk=None):
        user = self.get_object()
        serializer = UserSerializer(user)
        user.name = serializer.data['name']
        user.email = serializer.data['email']
        user.save()
        return Response({'status': 'User details updated'})


class ProductView(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer



