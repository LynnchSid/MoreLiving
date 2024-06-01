from django.shortcuts import render
from .serializers import ReviewSerializer
from .models import Review
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status



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
class ReviewListCreate(BaseAPIView):
    serializer_class = ReviewSerializer
    queryset = Review.objects.all()
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['restaurant']

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context=self.get_serializer_context())
        if serializer.is_valid():
            self.perform_create(serializer)
            response_data = {
                "success": True,
                "message": "Review has been created.",
                "data": serializer.data
            }
            return Response(response_data, status=201)
        else:
            response_data = {
                "success": "True",
                "message": "Invalid data",
                "errors": serializer.errors
            }
            return Response(response_data, status=400)
        

class ReviewDetail(BaseAPIView):
    serializer_class = ReviewSerializer
    queryset = Review.objects.all()
    permission_classes = [IsAuthenticated]

    def patch(self, request, pk, *args, **kwargs):
        try:
            review = Review.objects.get(pk=pk)
        except Review.DoesNotExist:
            return Response({"error": "Review not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = self.serializer_class(review, data=request.data, partial=True, context=self.get_serializer_context())
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        
class ReviewList(BaseAPIView):
    serializer_class = ReviewSerializer
    queryset = Review.objects.all()
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset().all()
        serializer = self.serializer_class(queryset, many=True, context=self.get_serializer_context())
        return Response(serializer.data)
    
class ReviewListByRestaurant(BaseAPIView):
    serializer_class = ReviewSerializer
    queryset = Review.objects.all()
    permission_classes = [IsAuthenticated]

    def get(self, request, pk, *args, **kwargs):
        queryset = self.get_queryset().filter(restaurant=pk)
        serializer = self.serializer_class(queryset, many=True, context=self.get_serializer_context())
        return Response(serializer.data)
