from django.urls import path
from app_api import views


urlpatterns = [
    path('app/', views.Rest_Api_Test),
]