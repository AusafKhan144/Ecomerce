from django.shortcuts import render,redirect
from django.views import View
# Create your views here.

class SigninView(View):
    def get(request,*args, **kwargs):
        return render(request,'authenticate/signin.html',{})
    
    # def post(request,*args, **kwargs):
    #     return redirect('store')



class SignupView():
    pass

class SignoutView():
    pass