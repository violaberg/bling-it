from django.urls import path
from . import views


urlpatterns = [
    path('', views.reviews, name='reviews'),
    path('submit_review/', views.submit_review, name='submit_review'),
]
