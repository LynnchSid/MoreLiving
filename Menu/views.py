from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Ingredient, MenuItemType, MenuItem
from .serializers import MenuItemTypeSerializer, IngredientSerializer, MenuItemSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status

class BaseAPIView(APIView):
    serializer_class = None
    queryset = None
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = []  # Initialize as an empty list

    def get_serializer_context(self):
        return {'request': self.request}

    def get_queryset(self):
        return self.queryset

    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset().all()
        # Apply filters
        for backend in list(self.filter_backends):
            queryset = backend().filter_queryset(self.request, queryset, self)
        serializer = self.serializer_class(queryset, many=True, context=self.get_serializer_context())
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context=self.get_serializer_context())
        if serializer.is_valid():
            instance = serializer.save()
            response_data = {
                "success": True,
                "message": "Created successfully.",
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

    def delete(self, request, *args, **kwargs):
        instance = self.get_queryset().filter(pk=request.data['id']).first()
        if instance:
            instance.delete()
            response_data = {
                "success": True,
                "message": "Deleted successfully."
            }
            return Response(response_data, status=200)
        else:
            response_data = {
                "success": False,
                "message": "Instance not found."
            }
            return Response(response_data, status=404)

    def patch(self, request, *args, **kwargs):
        instance = self.get_queryset().filter(pk=request.data['id']).first()
        if instance:
            serializer = self.serializer_class(instance, data=request.data, partial=True, context=self.get_serializer_context())
            if serializer.is_valid():
                serializer.save()
                response_data = {
                    "success": True,
                    "message": "Updated successfully.",
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
        else:
            response_data = {
                "success": False,
                "message": "Instance not found."
            }
            return Response(response_data, status=404)


class MenuItemTypeListCreate(BaseAPIView):
    serializer_class = MenuItemTypeSerializer
    queryset = MenuItemType.objects.all()

class MenuItemListCreate(BaseAPIView):
    serializer_class = MenuItemSerializer
    queryset = MenuItem.objects.all()
    filterset_fields = ['restaurant', 'type', 'name', 'price', 'description', 'ingredients__name']  # Adjusted fields

    def get_queryset(self):
        restaurant_id = self.request.query_params.get('restaurant_id')
        if restaurant_id:
            return self.queryset.filter(restaurant_id=restaurant_id)
        return self.queryset
