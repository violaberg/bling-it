from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('faq/', views.faq, name='faq'),
    path('', views.subscribe_to_newsletter, name='subscribe_to_newsletter'),
    path('privacy_policy/', views.privacy_policy, name='privacy_policy'),
]
