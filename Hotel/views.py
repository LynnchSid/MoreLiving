from rest_framework import generics
from .models import HotelCategory, Hotel, Hotelimage
from .serializers import HotelCategorySerializer, HotelSerializer, HotelimageSerializer
from .filters import HotelCategoryFilter, HotelFilter, HotelimageFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework.views import APIView

class BaseAPIView(APIView):
    serializer_class = None
    queryset = None
    permission_classes = []
    parser_classes = [MultiPartParser, FormParser]
    filter_backends = [DjangoFilterBackend]
    filterset_class = None

    def get_serializer_context(self):
        return {'request': self.request}

    def get_queryset(self):

        queryset = self.queryset
        filterset = self.filterset_class(self.request.GET, queryset=queryset)
        if filterset.is_valid():
            queryset = filterset.qs
        return queryset

    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset().all()
        serializer = self.serializer_class(queryset, many=True, context=self.get_serializer_context())
        return Response(serializer.data)
    
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context=self.get_serializer_context())
        if serializer.is_valid():
            instance = serializer.save()
            data = serializer.data
            response_data = {
                "success": True,
                "message": f"{self.serializer_class.Meta.model.__name__} has been created.",
                "data": data
            }
            return Response(response_data, status=201)
        else:
            response_data = {
                "success": False,
                "message": "Invalid data",
                "errors": serializer.errors
            }
            return Response(response_data, status=400)
        
    def delete(self, request, *args, **kwargs):
        hotel_id = kwargs.get('pk')
        try:
            instance = Hotel.objects.get(pk=hotel_id)
            instance.delete()
            response_data = {
                "success": True,
                "message": f"{self.serializer_class.Meta.model.__name__} has been deleted."
            }
            return Response(response_data, status=204)
        except Hotel.DoesNotExist:
            response_data = {
                "success": False,
                "message": f"{self.serializer_class.Meta.model.__name__} not found."
            }
            return Response(response_data, status=404)
            
    def patch(self, request, *args, **kwargs):
        hotel_id = kwargs.get('pk')
        try:
            instance = Hotel.objects.get(pk=hotel_id)
            serializer = self.serializer_class(instance, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                response_data = {
                    "success": True,
                    "message": f"{self.serializer_class.Meta.model.__name__} has been updated.",
                    "data": serializer.data
                }
                return Response(response_data, status=200)
            else:
                response_data = {
                    "success": False,
                    "message": "Invalid data",
                    "errors": serializer.errors
                }
                return Response(response_data, status=400)
        except Hotel.DoesNotExist:
            response_data = {
                "success": False,
                "message": f"{self.serializer_class.Meta.model.__name__} not found."
            }
            return Response(response_data, status=404)

class HotelCategoryListCreate(BaseAPIView):
    serializer_class = HotelCategorySerializer
    queryset = HotelCategory.objects.all()
    permission_classes = [IsAuthenticated]
    filterset_class = HotelCategoryFilter

class HotelListCreate(BaseAPIView):
    serializer_class = HotelSerializer
    queryset = Hotel.objects.all()
    permission_classes = [IsAuthenticated]
    filterset_class = HotelFilter

class HotelimageListCreate(BaseAPIView):
    serializer_class = HotelimageSerializer
    queryset = Hotelimage.objects.all()
    permission_classes = [IsAuthenticated]
    filterset_class = HotelimageFilter
