from django.urls import path
import ThresholdWeightApp.views as views

app_name = 'threshold_weight_app'
urlpatterns = [
    path('thresholds-weights/', views.ThresholdWeightListView.as_view()),
    path('threshold-weight/create/', views.ThresholdWeightCreateView.as_view()),
    path('threshold-weight/update/<int:pk>', views.ThresholdWeightUpdateView.as_view()),
    path('threshold-weight/delete/<int:pk>', views.ThresholdWeightDeleteView.as_view()),
]
