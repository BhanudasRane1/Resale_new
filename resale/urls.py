from django.contrib import admin

from . import views

from django.contrib import admin
from django.urls import path, include
from .views import *


urlpatterns = [
    # path('',views.index,name="index"),
    path('', Index_View.as_view(), name='index_url'),
    path('shop', Shop_View.as_view(), name='shop_url'),
    path('about', About_View.as_view(), name='about_url'),
    path('cart', Cart_View.as_view(), name='cart_url'),
    path('checkout', Checkout_View.as_view(), name='checkout_url'),
    path('contact', Contact_View.as_view(), name='contact_url'),
    path('detail-product', Detail_product_View.as_view(), name='detail-product_url'),
    path('faq', Faq_View.as_view(), name='faq_url'),
    path('privacy', Privacy_View.as_view(), name='privacy_url'),
    path('setting', Setting_View.as_view(), name='setting_url'),
    path('terms', Terms_View.as_view(), name='terms_url'),
    path('transaction', Transaction_View.as_view(), name='transaction_url'),
    path('sell/', Sell_View.as_view(), name='sell_url'),
   

    

    
]