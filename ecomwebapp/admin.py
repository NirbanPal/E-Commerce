from django.contrib import admin
from django.utils.html import format_html
from django.urls import reverse
from ecomwebapp.models import *
 
# Register your models here.
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('id','user','name','locality','city','zipcode','state')

class ProductAdmin(admin.ModelAdmin):
    list_display = ('id','title','selling_price','discounted_price','description','brand','catagoty','stock','product_image')   

class CartAdmin(admin.ModelAdmin):
    list_display = ('id','user','product','quantity')

class OrderPlacesAdmin(admin.ModelAdmin):
    readonly_fields = ('order_date',)
    list_display = ('id','user','customer','customer_info','product','product_info','quantity','status','order_date')

    def customer_info(self,obj):
        #args here is basically a link object
        link = reverse("admin:ecomwebapp_customer_change",args=[obj.customer.pk])
        #showing as a link by clicking that customer details wil be open
        return format_html('<a href="{}">{}</a>',link,obj.customer.name)


    def product_info(self,obj):
        #args here is basically a link object
        link = reverse("admin:ecomwebapp_product_change",args=[obj.product.pk])
        #showing as a link by clicking that customer details wil be open
        return format_html('<a href="{}">{}</a>',link,obj.product.title)


admin.site.register(Customer,CustomerAdmin)
admin.site.register(Product,ProductAdmin)
admin.site.register(Cart,CartAdmin)
admin.site.register(OrderPlaces,OrderPlacesAdmin)






