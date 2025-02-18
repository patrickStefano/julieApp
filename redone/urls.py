from django.urls import path
from . import views


urlpatterns = [
  path('', views.home, name='home'),
  path('gallery_page/', views.gallery_page, name='gallery_page'),
  path('photo/<str:pk>/', views.photo, name='photo'),
  path('adding', views.adding, name='adding')
]