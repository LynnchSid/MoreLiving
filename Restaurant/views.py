from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import  IsAdminUser
from .serializers import CategorySerializer, RestaurantSerializer, RestaurantImageSerializer
from django_filters.rest_framework import DjangoFilterBackend
from .models import Category, Restaurant, RestaurantImage
from rest_framework import status
from django_filters.rest_framework import DjangoFilterBackend
from .pagination import CustomPagination



class BaseAPIView(APIView):
    serializer_class = None
    queryset = None
    permission_classes = []
    parser_classes = [MultiPartParser, FormParser]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['location','delivery']
    pagination_class = CustomPagination
    

    def get_serializer_context(self):
        return {'request': self.request}

    def get_queryset(self):
        return self.queryset

    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset().all()
        # Apply filters
        for backend in list(self.filter_backends):
            queryset = backend().filter_queryset(self.request, queryset, self) 
        paginator = self.pagination_class()
        paginated_queryset = paginator.paginate_queryset(queryset, request)
        serializer = self.serializer_class(paginated_queryset, many=True, context=self.get_serializer_context())
        return paginator.get_paginated_response(serializer.data)

class CategoryListCreate(BaseAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context=self.get_serializer_context())
        if serializer.is_valid():
            instance = serializer.save()
            data = serializer.data
            response_data = {
                "success": True,
                "message": "Category has been created.",
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


class RestaurantListCreate(BaseAPIView):
    serializer_class = RestaurantSerializer
    queryset = Restaurant.objects.all()
    permission_classes = [IsAdminUser]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['category', 'location']

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context=self.get_serializer_context())
        if serializer.is_valid():
            instance = serializer.save()
            data = serializer.data
            response_data = {
                "success": True,
                "message": "Restaurant has been created.",
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

    def delete(self, request, pk, *args, **kwargs):
        try:
            restaurant = Restaurant.objects.get(pk=pk)
            restaurant.delete()
            return Response({"message": "Restaurant deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
        except Restaurant.DoesNotExist:
            return Response({"error": "Restaurant not found"}, status=status.HTTP_404_NOT_FOUND)

    def patch(self, request, pk, *args, **kwargs):
        try:
            restaurant = Restaurant.objects.get(pk=pk)
        except Restaurant.DoesNotExist:
            return Response({"error": "Restaurant not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = self.serializer_class(restaurant, data=request.data, partial=True,
                                           context=self.get_serializer_context())
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RestaurantDetail(BaseAPIView):
    serializer_class = RestaurantSerializer
    queryset = Restaurant.objects.all()
    permission_classes = [IsAdminUser]

    def delete(self, request, pk, *args, **kwargs):
        try:
            restaurant = self.get_object()
            restaurant.delete()
            return Response({"message": "Restaurant deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
        except Restaurant.DoesNotExist:
            return Response({"error": "Restaurant not found"}, status=status.HTTP_404_NOT_FOUND)

    def patch(self, request, *args, **kwargs):
        restaurant = self.get_object()
        serializer = self.serializer_class(restaurant, data=request.data, partial=True, context=self.get_serializer_context())
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class RestaurantImageListCreate(BaseAPIView):
    serializer_class = RestaurantImageSerializer
    queryset = RestaurantImage.objects.all()
    permission_classes = [IsAdminUser]

    def post(self, request, *args, **kwargs):   
        serializer = self.serializer_class(data=request.data, context=self.get_serializer_context())
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class RestaurantImageDetail(BaseAPIView):
    serializer_class = RestaurantImageSerializer
    queryset = RestaurantImage.objects.all()
    permission_classes = [IsAdminUser]

    def delete(self, request, pk, *args, **kwargs):
        try:
            image = self.get_object()
            image.delete()
            return Response({"message": "Image deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
        except Restaurant.DoesNotExist:
            return Response({"error": "Image not found"}, status=status.HTTP_404_NOT_FOUND)
        
    def patch(self, request, *args, **kwargs):
        image = self.get_object()
        serializer = self.serializer_class(image, data=request.data, partial=True, context=self.get_serializer_context())
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    