from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def login(request):
     """
     just return a welcome message for now
     """

     return render(request,'core/base.html',{})
