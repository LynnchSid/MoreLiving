from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UserProfileSerializer
from .models import UserProfile
from rest_framework.permissions import IsAuthenticated

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
    
class UserProfileListCreate(BaseAPIView):
    serializer_class = UserProfileSerializer
    queryset = UserProfile.objects.all()
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context=self.get_serializer_context())
        if serializer.is_valid():
            self.perform_create(serializer)
            response_data = {
                "success": True,
                "message": "User profile has been created.",
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
        
class UserProfileDetail(BaseAPIView):
    serializer_class = UserProfileSerializer
    queryset = UserProfile.objects.all()
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)

    def patch(self, request, pk, *args, **kwargs):
        try:
            profile = UserProfile.objects.get(pk=pk)
        except UserProfile.DoesNotExist:
            return Response({"error": "User profile not found"}, status=404)

        serializer = self.serializer_class(profile, data=request.data, partial=True, context=self.get_serializer_context())
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        else:
            return Response(serializer.errors, status=400)
        
