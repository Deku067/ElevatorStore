from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('products/', views.product_list, name='product_list'),
    path('about/', views.aboutus, name='about_us'),
    path('contacts/', views.contact, name='contacts'),
    path('checkout/', views.checkout, name='checkout'),
    # path('add_to_cart/', views.Add_to_cart, name='add_to_cart'),
]
