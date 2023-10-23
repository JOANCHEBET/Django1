from django.urls import path
from . import views

urlpatterns = [
    path('', views.welcome, name='welcome'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact_us, name='contact us'),
    path('register/', views.register, name='register'),
]
