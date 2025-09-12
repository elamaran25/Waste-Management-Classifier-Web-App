from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Add this line
    path('classify/webcam/', views.classify_webcam_image, name='classify_webcam'),
    path('classify/upload/', views.classify_uploaded_image, name='classify_upload'),
]