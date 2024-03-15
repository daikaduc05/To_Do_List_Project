from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import authenticate,login
from .decorator import guest_only
@guest_only
def user_login(request):
    if(request.method == 'POST'):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username = username,password = password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            return redirect('error')
    return render(request,'login.html')