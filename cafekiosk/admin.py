from django.contrib import admin
from cafekiosk.models import OrderType, Menu, Option, Size, OrderList

admin.site.register(OrderType)
admin.site.register(Menu)
admin.site.register(Option)
admin.site.register(Size)
admin.site.register(OrderList)
