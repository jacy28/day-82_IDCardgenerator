from django.urls import path
from . import views

urlpatterns=[
    path('', views.create_idcard, name='create_idcard'),
    path('cards/', views.student_cards, name="student_cards"),
]