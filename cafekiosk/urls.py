from django.urls import path
from . import views

app_name = 'cafekiosk'

urlpatterns = [
    path("", views.MenuListView.as_view(), name="index"),
    path("<int:pk>", views.OptionDetailView.as_view(), name="detail"),
]