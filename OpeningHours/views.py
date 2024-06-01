from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import OpeningHourSerializer
from .models import OpeningHour
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
    
class OpeningHourListCreate(BaseAPIView):
    serializer_class = OpeningHourSerializer
    queryset = OpeningHour.objects.all()
    permission_classes = [IsAdminUser]

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
                "message": "Opening hour has been created.",
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
