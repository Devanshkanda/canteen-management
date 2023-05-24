from django.contrib import admin
from Stall.models import Product , Stall,Order,OrderItem,DeliveryInfo

admin.site.register(Product)
admin.site.register(Stall)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(DeliveryInfo)

