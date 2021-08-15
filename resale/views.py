from django.shortcuts import render
from django.conf import settings


from django.views.generic import View 
# Create your views here.

# def index(request):
#     return render(request,'index.html')

class Index_View(View):             
     def get(self,request):
         template = 'index.html'
         return render(request, template)
class About_View(View):             
     def get(self,request):
         template = 'about.html'
         return render(request, template)

class Cart_View(View):             
     def get(self,request):
         template = 'cart.html'
         return render(request, template)

class Checkout_View(View):             
     def get(self,request):
         template = 'checkout.html'
         return render(request, template)

class Contact_View(View):             
     def get(self,request):
         template = 'contact.html'
         return render(request, template)

class Detail_product_View(View):             
     def get(self,request):
         template = 'detail-product.html'
         return render(request, template)
class Faq_View(View):             
     def get(self,request):
         template = 'faq.html'
         return render(request, template)
          
class Privacy_View(View):             
     def get(self,request):
         template = 'privacy.html'
         return render(request, template)
          
class Setting_View(View):             
     def get(self,request):
         template = 'setting.html'
         return render(request, template)
          
class Shop_View(View):             
     def get(self,request):
         template = 'shop.html'
         return render(request, template)
          
class Terms_View(View):             
     def get(self,request):
         template = 'terms.html'
         return render(request, template)
          
class Transaction_View(View):             
     def get(self,request):
         template = 'transaction.html'
         return render(request, template)
          



