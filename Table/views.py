from django.shortcuts import render
from .serializers import TableSerializer
from .models import Table
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser

# Create your views here.
class BaseAPIView(APIView):
    serializer_class = None
    queryset = None
    permission_classes = []

    def get_serializer_context(self):
        return {'request': self.request}

    def get_queryset(self):
        return self.queryset

    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset().all()
        serializer = self.serializer_class(queryset, many=True, context=self.get_serializer_context())
        return Response(serializer.data)
class TableListCreate(BaseAPIView):
    serializer_class = TableSerializer
    queryset = Table.objects.all()
    permission_classes = [IsAdminUser]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['restaurant']

    def get_queryset(self):
        restaurant_id = self.request.query_params.get('restaurant_id')
        if restaurant_id:
            return self.queryset.filter(restaurant_id=restaurant_id)
        return self.queryset

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context=self.get_serializer_context())
        if serializer.is_valid():
            instance = serializer.save()
            response_data = {
                "success": True,
                "message": "Table has been created.",
                "data": serializer.data
            }
            return Response(response_data, status=201)
        else:
            response_data = {
                "success": False,
                "message": "Invalid data",
                "errors": serializer.errors
            }
            return Response(response_data, status=400)
class AvailableTablesView(generics.ListAPIView):
    serializer_class = TableSerializer
    queryset = Table.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['restaurant']

    def get_queryset(self):
        restaurant_id = self.request.query_params.get('restaurant_id')
        booking_date = self.request.query_params.get('booking_date')
        booking_time = self.request.query_params.get('booking_time')
        if restaurant_id and booking_date and booking_time:
            booked_tables = Booking.objects.filter(
                restaurant_id=restaurant_id,
                bookingDate=booking_date,
                bookingTime=booking_time
            ).values_list('table_id', flat=True)
            return self.queryset.filter(restaurant_id=restaurant_id).exclude(id__in=booked_tables)
        return self.queryset