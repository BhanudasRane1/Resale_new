from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User,auth

from django.views.generic import View 

# Create your views here.

# def login(request):
    # if request.method=='POST':
    #      username = request.POST['username']
    #      password= request.POST['password'] 

    #      user = auth.authenticate(username=username,password=password)

    #      if user is not None:
    #          auth.login(request,user)
    #          messages.error(request,'Invalid credentials....Please Enter valid credentials')
    #          return redirect("/")
    #      else:
    #         messages.error(request,'Invalid credentials....Please Enter valid credentials')
    #         return redirect('login')

    # else: 
        
        # return render(request,'login.html')


# def register(request):
    # if request.method == 'POST':
    #     first_name = request.POST['first_name']
    #     username = request.POST['username']
    #     password1= request.POST['password1']
    #     password2= request.POST['password2']
    #     email = request.POST['email']
        
    #     if password1==password2:
    #         if User.objects.filter(username=username).exists():
    #             messages.error(request,'Username is already taken')
    #             return redirect('register')
    #         elif User.objects.filter(email=email).exists():
    #             messages.error(request,'Email is already taken')
    #             return redirect('register')
    #         else:
    #             user =User.objects.create_user(username=username,password=password1,email=email,first_name=first_name)
    #             user.save()
    #             messages.error(request,'Account created successfully')
    #             return redirect('login')
    #     else:
    #         messages.error(request,'Please enter same password')
    #         return redirect('register')
    #     return redirect('/')
    # return render(request,"register.html")



# def logout(request):
#     auth.logout(request)
#     return redirect('/')



class Register_View(View):
    def get(self,request):
        template = 'register.html'
        return render(request,template)

    def post(self,request):
        template = 'register.html'
        if request.method == 'POST':
            first_name = request.POST['first_name']
            username = request.POST['username']
            password1= request.POST['password1']
            password2= request.POST['password2']
            email = request.POST['email']
        
            if password1==password2:
                if User.objects.filter(username=username).exists():
                    messages.error(request,'Username is already taken')
                    return redirect('register_url')
                elif User.objects.filter(email=email).exists():
                    messages.error(request,'Email is already taken')
                    return redirect('register_url')
                else:
                    user =User.objects.create_user(username=username,password=password1,email=email,first_name=first_name)
                    user.save()
                    messages.error(request,'Account created successfully')
                    return redirect('login_url')
            else:
                messages.error(request,'Please enter same password')
                return redirect('register_url')
            return redirect('/')
        return render(request, template)

class Login_View(View):
    def get(self,request):
        template= 'login.html'
        return render(request,template )


    def post(self,request):
        template = 'login.html'
        if request.method=='POST':
            username = request.POST['username']
            password= request.POST['password'] 
            user = auth.authenticate(username=username,password=password)
            if user is not None:
                auth.login(request,user)
                messages.error(request,'Invalid credentials....Please Enter valid credentials')
                return redirect("/")
            else:
                messages.error(request,'Invalid credentials....Please Enter valid credentials')
                return redirect('login')

        else:
            return render(request, template)

class Logout_View(View):           
    def get(self,request):
        template = 'logout.html'
        auth.logout(request)
        return render(request, template)
