from django.urls import path
from . import views
from profiles.views import add_to_wishlist


urlpatterns = [
    path('', views.all_gemstones, name='gemstones'),
    path('<int:gemstone_id>/', views.gemstone_detail, name='gemstone_detail'),
    path('add_to_wishlist/', views.add_to_wishlist, name='add_to_wishlist'),
    path('add/', views.add_gemstone, name='add_gemstone'),
    path('edit/<int:gemstone_id>/', views.edit_gemstone, name='edit_gemstone'),
    path(
        'delete/<int:gemstone_id>/', views.delete_gemstone, name='delete_gemstone'
        ),
]
