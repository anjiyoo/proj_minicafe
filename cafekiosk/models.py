from django.db import models
from django.utils import timezone

# 주문 타입
# store/packaging/delivery
class OrderType(models.Model):
    # OrderType column
    order_type_name = models.CharField(max_length=100)
    def __str__(self):
       return self.order_type_name


# 메뉴 
# Caffe Americano/Caffe Latte/Cappuccino/Vanilla Bean Latte/Starbucks Dolce Latte/Coffee Starbucks Double Shot
# Cool Lime Starbucks Fizzio/Light Pink Grapefruit Fizzio/Mango Banana Blended/Espresso Frappuccino
class Menu(models.Model):
    # Menu column
    menu_name = models.CharField(max_length=100)
    menu_price = models.IntegerField(default=0)
    def __str__(self):
       return self.menu_name

    

# 음료 추가옵션
# hot/ice
class Option(models.Model):
    # Option column
    option_name = models.CharField(max_length=100)
    def __str__(self):
        return self.option_name
      

# 사이즈 추가옵션
# tall/grande/venti
class Size(models.Model):
    # Size column
    size_name = models.CharField(max_length=100)
    size_price = models.IntegerField(default=0)
    def __str__(self):
        return self.size_name
      


# 주문 리스트
class OrderList(models.Model):
    # OrderType 참조
    order_type_name = models.ForeignKey(OrderType, on_delete=models.CASCADE)
    # Menu 참조
    menu_name = models.ForeignKey(Menu, on_delete=models.CASCADE)
    # Option 참조
    option_name = models.ForeignKey(Option, on_delete=models.CASCADE)
    # Size 참조
    size_name = models.ForeignKey(Size, on_delete=models.CASCADE)

    # OrderList column
    order_memo = models.CharField(max_length=100)
    menu_count = models.IntegerField(default=0)
    total_price = models.IntegerField(default=0)
    date = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.order_memo
