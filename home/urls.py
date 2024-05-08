from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('', views.about, name='about'),
    path('', views.faq, name='faq'),
    path('', views.privacy_policy, name='privacy_policy'),
    
]
