from django.urls import path

from . import views
from .views import DetectionView, SegmentationView,GeneralView

urlpatterns = [
    path('', views.PatListView.as_view(), name='Patient'),
    path('exercise/', views.ExListView.as_view(), name='Exercise'),
    path('SegmentationDataset/', views.detectionview, name="segmendata"),
    path('addDetection/',DetectionView.as_view() , name='detection'),
    path('addSegmentation/', SegmentationView.as_view(), name='segmentation'),
    path('dataGeneral/', GeneralView.as_view(), name='dataGeneral'),
]
