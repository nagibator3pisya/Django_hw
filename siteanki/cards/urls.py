from django.urls import path
from . import views

urlpatterns = [
    path('', views.catalog),
    path('catalog/<int:card_id>/', views.get_card_by_id),
    path('catalog/<slug:slug>/', views.get_category_by_name),
]
