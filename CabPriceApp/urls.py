from django.urls import path
from . import views
from rest_framework import routers

app_name = 'cab_price_app'
urlpatterns = [
]

router = routers.SimpleRouter()
router.register('threshold', views.PriceWeightViewSet)
urlpatterns += router.urls
