from django.urls import path
from . import views

urlpatterns = [
    path('landing-page', views.landing_page, name='landing_page'),
    path('browse-books/', views.browse_books, name='browse_books'),
]
