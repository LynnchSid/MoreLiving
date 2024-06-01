from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import PaymentSerializer
from .models import Payment
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import RetrieveUpdateDestroyAPIView

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
    
class PaymentListCreate(BaseAPIView):
    serializer_class = PaymentSerializer
    queryset = Payment.objects.all()
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        if self.request.user.is_staff:
            return self.queryset.all()
        return self.queryset.filter(booking__user=self.request.user)

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context=self.get_serializer_context())
        if serializer.is_valid():
            instance = serializer.save()
            response_data = {
                "success": True,
                "message": "Payment has been processed.",
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
        
class PaymentDetail(RetrieveUpdateDestroyAPIView):
    serializer_class = PaymentSerializer
    queryset = Payment.objects.all()
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)
