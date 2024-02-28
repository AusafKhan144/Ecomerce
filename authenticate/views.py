from django.shortcuts import render,redirect
from django.views import View
from .forms import SigninForm
from django.contrib.auth import login,authenticate,logout
from django.contrib import messages
# Create your views here.

class SigninView(View):
    def get(self,request,*args, **kwargs):
        return render(request,'authenticate/signin.html',{'form': SigninForm()})
    
    def post(self, request, *args, **kwargs):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)           
            return redirect('store')
        else:
            messages.error(request,'User Does Not Exist')
            return render(request, 'authenticate/signin.html', {'form': SigninForm()})


class SignupView(View):
    pass

class SignoutView(View):
    pass