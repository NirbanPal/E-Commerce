from itertools import product
from django.shortcuts import render,redirect
from django.views import View #cause here we are using class based views
from .models import *
from .forms import CustomerRegistrationForm,LoginForm,MySetPasswordForm,CustomerProfileForm
from django.contrib import messages
from django.db.models import Q

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from django.core import serializers
# for function based view
from django.contrib.auth.decorators import login_required
# for class based view
from django.utils.decorators import method_decorator

import razorpay
from django.conf import settings


class ProductView(View):
    def get(self,request):
        top_wear = Product.objects.filter( catagoty = 'TW')
        bottom_wear = Product.objects.filter( catagoty = 'BW')
        mobile = Product.objects.filter( catagoty = 'M')

        context = {
            'topwear' : top_wear,
            'bottomwear' : bottom_wear,
            'mobile' : mobile
        }

        return render(request,'home.html',context)

class ProductDetailView(View):
    def get(self,request,pk):
        productdetail = Product.objects.get(pk=pk)
        item_already_in_cart = False
        if request.user.is_authenticated:
            item_already_in_cart = Cart.objects.filter(Q(product=productdetail.id) & Q(user=request.user)).exists()
        context = {
            'productdetail':productdetail,
            'item_already_in_cart':item_already_in_cart
        }
        return render(request,'productdetail.html',context)



@login_required
def add_to_cart(request,id):
    user = request.user
    product_id = Product.objects.get(id=id)
    print(product_id)
    Cart(user=user,product=product_id).save()

    return redirect('/cart')

@login_required
def showcart(request):
    if request.user.is_authenticated:
        user = request.user
        cart_products = Cart.objects.filter(user=user)
        amount = 0.0
        shipping_amount = 70.00
        total_amount = 0.0
        cart_product = [pro for pro in Cart.objects.all() if pro.user == user]
        if cart_product:
            for ele in cart_product:
                each_product_amount = (ele.quantity * ele.product.discounted_price)
                amount += each_product_amount
            total_amount = amount + shipping_amount

            context={
                'cart_products':cart_products,
                'amount':amount,
                'total_amount':total_amount,
            }
            return render(request,'showcart.html',context)  
        else:
            context = {
                'empty_cart': 'Your Cart Is Empty.Please Add Products'
            }
            return render(request,'showcart.html',context)  

@csrf_exempt
def plus_cart(request):
    if request.method == 'GET':
        prod_id = request.GET['prod_id']
        cart_prod = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))    
        cart_prod.quantity+=1  
        cart_prod.save() 

        amount = 0.0
        shipping_amount = 70.00
        cart_product = [pro for pro in Cart.objects.all() if pro.user == request.user]

        for ele in cart_product:
            each_product_amount = (ele.quantity * ele.product.discounted_price)
            amount += each_product_amount
        total_amount = amount + shipping_amount

        data ={
            'total_amount': total_amount,
            'cart_quant' : cart_prod.quantity,
            'amount': amount
        }
        return JsonResponse(data)



@csrf_exempt
def minus_cart(request):
    if request.method == 'GET':
        prod_id = request.GET['prod_id']
        cart_prod = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))    
        if cart_prod.quantity > 1:
            cart_prod.quantity-=1  
            cart_prod.save() 

        amount = 0.0
        shipping_amount = 70.00
        cart_product = [pro for pro in Cart.objects.all() if pro.user == request.user]

        for ele in cart_product:
            each_product_amount = (ele.quantity * ele.product.discounted_price)
            amount += each_product_amount
        total_amount = amount + shipping_amount

        data ={
            'total_amount': total_amount,
            'cart_quant' : cart_prod.quantity,
            'amount': amount
        }
        return JsonResponse(data)    




@csrf_exempt
def remove_cart(request):
    if request.method == 'GET':
        prod_id = request.GET['prod_id']
        cart_prod = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))    
        cart_prod.delete() 

        amount = 0.0
        shipping_amount = 70.00
        cart_product = [pro for pro in Cart.objects.all() if pro.user == request.user]

        for ele in cart_product:
            each_product_amount = (ele.quantity * ele.product.discounted_price)
            amount += each_product_amount
        total_amount = amount + shipping_amount

        data ={
            'total_amount': total_amount,
            'amount': amount
        }
        return JsonResponse(data)        


def buy_now(request):
 return render(request, 'buynow.html')

@method_decorator(login_required,name='dispatch')
class ProfileView(View):
    def get(self,request):
        form = CustomerProfileForm( )
        context={
            'form':form,
            'active': 'btn-primary'
        }
        return render(request,'profile.html',context)

    def post(self,request):
        form = CustomerProfileForm(request.POST)
        if form.is_valid():
            usr = request.user
            name = form.cleaned_data['name']
            locality = form.cleaned_data['locality']
            city = form.cleaned_data['city']
            state = form.cleaned_data['state']
            zipcode = form.cleaned_data['zipcode']
            reg = Customer(user=usr,name=name,locality=locality,city=city,state=state,zipcode=zipcode)
            reg.save()
            messages.success(request,"Congtatulations!! your Profile Details is saved")

        return render(request,'profile.html',{'form':form , 'active':'btn-success'})  
     
      





@login_required
def address(request):
    address = Customer.objects.filter(user=request.user)
    context={
        'address':address,
        'active':'btn-primary'
    }
    return render(request, 'address.html',context)

@login_required
def orders(request):
    placed_orders = OrderPlaces.objects.filter(user = request.user)

    return render(request, 'orders.html',{'placed_orders':placed_orders})


def mobile(request,data='None'):
    mobile_brands = Product.objects.filter(catagoty='M').values('brand').distinct()
    mobiles=""
    if data == 'None':
        mobiles = Product.objects.filter(catagoty='M')
    elif data=='Moto' or data=='SAMSUNG' or data=='NOKIA' or data=='OPPO' or data=='Xiomi':
        mobiles = Product.objects.filter(catagoty = 'M').filter(brand=data)     
    context = {
        'mobiles': mobiles,
        'mobile_brands': mobile_brands,
    }    
    return render(request, 'mobile.html', context)

class CustomerRegistrationView(View):
    def get(self,request):
        form = CustomerRegistrationForm()
        return render(request,'customerregistration.html',{'form':form})

    def post(self,request):
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
            messages.success(request,"Congtatulations!! you have registered successfully..")
            form.save()
        return render(request,'customerregistration.html',{'form':form})    


@login_required
def checkout(request):
    user = request.user 
    address = Customer.objects.filter(user=user)
    cart_items = Cart.objects.filter(user=user)
    amount = 0.0
    shipping_amount = 70.00
    cart_product = [pro for pro in Cart.objects.all() if pro.user == user]

    if cart_product:
        for ele in cart_product:
            each_product_amount = (ele.quantity * ele.product.discounted_price)
            amount += each_product_amount
        total_amount = amount + shipping_amount

    client = razorpay.Client(auth = (settings.KEY , settings.SECRET))
    payment = client.order.create({'amount': total_amount * 100,'currency':'INR','payment_capture': 1})

    context ={
        'address': address,
        'cartitems': cart_items,
        'totalamount': total_amount,
        'payment':payment
    }
    return render(request, 'checkout.html',context)

@login_required
def payment_done(request):
    user = request.user
    custid = request.GET.get('custid') 
    customer = Customer.objects.get(id=custid)   
    cart = Cart.objects.filter(user=user)
    print(cart)
    for prod in cart:
        OrderPlaces(user=user,customer = customer,product=prod.product,quantity=prod.quantity).save()
        print(prod)
        prod.delete()
    return redirect('/orders')    


class MySetPasswordForm(MySetPasswordForm):
    
    def save(self, *args, commit=True, **kwargs):
        user = super().save(*args, commit=False, **kwargs)
        user.is_active = True
        if commit:
            user.save()
        return user
