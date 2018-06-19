#from django.http import HttpResponseRedirect
#from django.shortcuts import get_object_or_404, render
#from django.urls import reverse
#from django.views import generic
#from django.utils import timezone

#from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .forms import RegisterForm

def register(request):
    if request.method == 'POST':
        form=RegisterForm(request.POST)

        #验证数据的合法性
        if form.is_valid():
            form.save()
            return redirect('/')
    else: #请求不是POST，第一次访问注册页，展示空表单
        form=RegisterForm()
    return render(request, 'users/register.html', context={'form':form})

def index(request):
    return render(request, 'users/index.html')