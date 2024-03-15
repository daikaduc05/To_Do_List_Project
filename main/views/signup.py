from django.shortcuts import render,redirect
from django.contrib.auth import login
from .decorator import guest_only
from django.contrib import messages
from django.utils import timezone
from main.models import users
@guest_only
def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password_confirm = request.POST['password_confirm']
        if password == password_confirm:
            user = users.objects.create_user(username=username, email=email, password=password, join_at = timezone.now())
            login(request, user)
            messages.success(request, 'Đăng ký thành công!')
            return redirect('login')  
        else: 
            messages.error(request, 'Mật khẩu không khớp.')
    return render(request, 'signup.html')