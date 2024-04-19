from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_gemstones, name='gemstones'),
    path('<gemstone_id>', views.gemstone_detail, name='gemstone_detail'),
]
