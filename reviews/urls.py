from django.urls import path
from . import views


urlpatterns = [
    path('', views.reviews, name='reviews'),
    path('delete-review/<int:review_id>/', views.delete_review, name='delete_review'),
]
