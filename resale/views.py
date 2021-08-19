from django.shortcuts import render,redirect
from django.conf import settings
from django.contrib import messages
from .forms import *
from math import ceil
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
         
class Sell_View(View):
    def get(self,request):
         template = 'sell.html'
         sell_form = sell_product_form()

         context= {
             'form': sell_form,
         }

         return render(request, template,context)

    def post(self,request):
        template= 'sell.html'
        sell_form = sell_product_form(request.POST, request.FILES or None )
        if  sell_form.is_valid():
            sell_form = sell_form.save()
            messages.success(request, "Sell Book Order Placed Successfully!")
            return redirect('sell_url')
        else:
            messages.warning(request, "Something went Wrong!")
            return render(request, template) 
        
        
class Detail_product_View(View):
    def get(self,request):
         template = 'detail-product.html'
         sell_form = inquiry_form()

         context= {
             'form': sell_form,
         }

         return render(request, template,context)



# class Detail_product_View(View):
#     def get(self,request):
#         template = 'detail-product.html'
#         # inquiry_form = inquiry_form()
#         context= {
#             #  'form': inquiry_form,
#          }
         
#         return render(request, template , context)

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
        allProds=[]
        catProds = sell_product.objects.values('year','id')
        cats = {item['year'] for item in catProds}
        for cat in cats:
            prod = sell_product.objects.filter(year =cat)
            n = len(prod)
            nSlides = n // 4 + ceil((n / 4) - (n // 4))
            allProds.append([prod,range(1,nSlides),nSlides])
    
        params = {'allProds':allProds}
        template = 'shop.html'
        print(cats)
        print(nSlides)
        
        return render(request, template,params)
          
class Terms_View(View):             
     def get(self,request):
         template = 'terms.html'
         return render(request, template)
          
class Transaction_View(View):             
     def get(self,request):
         template = 'transaction.html'
         return render(request, template)
          



