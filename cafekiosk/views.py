from django.shortcuts import render
from django.http import HttpResponse
from .models import OrderType, Menu, Option, Size, OrderList
from django.urls import reverse
from django.views.generic import ListView, DetailView

class MenuListView(ListView):
    model = Menu
    template_name = "cafekiosk/menu_list.html"
    context_object_name = "menus"


class OptionDetailView(DetailView):
    model = Menu