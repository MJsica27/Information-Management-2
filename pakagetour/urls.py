from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('tour/<int:pk>/', views.tour_detail, name='tour_detail'),
    path('tour/<int:pk>/review/', views.review_submission, name='review_submission'),
]
