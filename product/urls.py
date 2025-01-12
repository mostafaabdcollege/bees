from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('add/', views.add_product, name='add_product'),
    path('edit/<int:product_id>/', views.edit_product, name='edit_product'),
    path('detail/<int:product_id>/', views.product_detail, name='product_detail'),
    path('delete/<int:product_id>/', views.delete_product, name='delete_product'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('search/', views.search, name='search'),
]
