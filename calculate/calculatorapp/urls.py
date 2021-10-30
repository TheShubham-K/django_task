
from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.index, name="index"),
    path('api/v1/calculator/', views.api),
    path('api/v1/calculator/result/', views.result),
]
