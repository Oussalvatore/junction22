from django.urls import path
from sustainable import views

urlpatterns = [
    path('fee/', views.get_estimates),
    path('deliveries/', views.delivery_list),
    path('deliveries/<int:pk>/', views.delivery_detail),
]
