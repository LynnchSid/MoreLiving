from django.urls import path
from .views import TableListCreate , AvailableTablesView

urlpatterns = [
    path('tables/', TableListCreate.as_view(), name='table-list-create'),
    path('tables/<int:pk>/', TableListCreate.as_view(), name='table-detail'),
    path('available-tables/', AvailableTablesView.as_view(), name='available-tables'),
]