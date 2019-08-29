from django.http import Http404
from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from django_filters import rest_framework as filters
from TestTask.filters import OrganizationFilter
from .serializers import CategorySerializer, NetworkSerializer, DistrictSerializer, ProductSerializer, \
    OrganizationSerializer, OrganizationProductPriceSerializer, OrganizationDetailSerializer, ProductDetailSerializer
from .models import Category, Network, District, Product, Organization, ProductPrice


class OrganizationListView(ListAPIView):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer


class OrganizationDetail(APIView):
    queryset = Organization.objects.all()
    serializer_class = OrganizationDetailSerializer

    def get_object(self, pk):
        try:
            return self.queryset.get(pk=pk)
        except Organization.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        posts_data = self.get_object(pk)
        serializer = OrganizationDetailSerializer(posts_data)
        return Response(serializer.data)


class OrganizationsByDistrictView(ListAPIView):
    serializer_class = OrganizationSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = OrganizationFilter

    def get_queryset(self):
        try:
            return Organization.objects.filter(districts=self.kwargs['pk'])
        except Organization.DoesNotExist:
            raise Http404

    def list(self, request, *args, **kwargs):
        f = OrganizationFilter(request.GET, queryset=self.get_queryset())
        serializer = OrganizationSerializer(f.qs.distinct(), many=True)
        return Response(serializer.data)


class ProductListView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductDetail(APIView):
    queryset = Product.objects.all()
    serializer_class = ProductDetailSerializer

    def get_object(self, pk):
        try:
            return Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        posts_data = self.get_object(pk)
        serializer = ProductDetailSerializer(posts_data)
        return Response(serializer.data)
