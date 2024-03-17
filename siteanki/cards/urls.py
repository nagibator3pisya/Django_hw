from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='home'), # главная страцица
    path('about/', views.about, name='about'),
    path('card_details/<int:card_id>/', views.card_details, name='card_details')

]
