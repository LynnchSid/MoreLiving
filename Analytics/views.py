from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.db.models import Count, Avg, Sum
from Restaurant.models import Restaurant
from Booking.models import Booking
from Review.models import Review
from Payment.models import Payment

class AnalyticsDashboardView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        total_restaurants = Restaurant.objects.count()
        total_bookings = Booking.objects.count()
        total_reviews = Review.objects.count()
        total_payments = Payment.objects.count()
        total_revenue = Payment.objects.aggregate(total_revenue=Sum('amount'))['total_revenue']
        average_rating_per_restaurant = Restaurant.objects.annotate(avg_rating=Avg('reviews__rating'))
        bookings_per_restaurant = Restaurant.objects.annotate(total_bookings=Count('bookings'))
        reviews_per_restaurant = Restaurant.objects.annotate(total_reviews=Count('reviews'))

        data = {
            'total_restaurants': total_restaurants,
            'total_bookings': total_bookings,
            'total_reviews': total_reviews,
            'total_payments': total_payments,
            'total_revenue': total_revenue,
            'average_rating_per_restaurant': [
                {'restaurant': restaurant.name, 'avg_rating': restaurant.avg_rating}
                for restaurant in average_rating_per_restaurant
            ],
            'bookings_per_restaurant': [
                {'restaurant': restaurant.name, 'total_bookings': restaurant.total_bookings}
                for restaurant in bookings_per_restaurant
            ],
            'reviews_per_restaurant': [
                {'restaurant': restaurant.name, 'total_reviews': restaurant.total_reviews}
                for restaurant in reviews_per_restaurant
            ],
        }

        return Response(data)
