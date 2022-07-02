from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('speciality', views.speciality, name='speciality'),
    path('popular', views.popular, name='popular'),
    path('gallery', views.gallery, name='gallery'),
    path('cart', views.cart, name='cart'),
    path('checkout', views.checkout, name='checkout'),
]