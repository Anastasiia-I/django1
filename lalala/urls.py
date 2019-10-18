from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='lalala-home'),
    path('about/', views.about, name='lalala-about'),
]