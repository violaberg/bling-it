from django.urls import path
from . import views
from profiles.views import add_to_wishlist

urlpatterns = [
    path('', views.all_gemstones, name='gemstones'),
    path('<gemstone_id>', views.gemstone_detail, name='gemstone_detail'),
    path('add_to_wishlist', views.add_to_wishlist, name='add_to_wishlist'),
]
