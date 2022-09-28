from django.urls import path
import CabPriceCoefficientApp.views as views

app_name = 'CabPriceCoefficientApp'
urlpatterns = [
    path('cab-price-coefficient/', views.CabPriceCoefficientView.as_view()),
]
