from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import task,users
from django.contrib import messages
# Create your views here.
def error(request):
    return render(request,'error.html')
def guest_only(view_func):
    def wrapper(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home')  
        return view_func(request, *args, **kwargs)
    return wrapper
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
def user_logout(request):
    logout(request)
    return redirect('login')
@login_required(login_url='login')
def home(request):
    userr = request.user
    taskk = task.objects.filter(who = userr.user_id)
    return render(request,'home.html',{'taskk' : taskk})
@login_required(login_url='login')
def create(request):
    userr = request.user
    if request.method == 'POST' :
        description = request.POST['description']
        priority = request.POST['priority']
        start_time = request.POST['start_time']
        deadline = request.POST['deadline']
        task.objects.create(
            who_id = userr.user_id,
            description = description,
            priority = priority,
            start_time = start_time,
            deadline = deadline,
            creat_at = timezone.now()
        )
        return redirect('home')
    else:
        return render(request,'create.html')
@login_required(login_url='login')
def edit(request,id_need_edit):
    task_edit = get_object_or_404(task, task_id=id_need_edit)
    if(task_edit.who_id == request.user.user_id):
        if(request.method == 'POST'):
            task_edit.description = request.POST.get('description')
            task_edit.priority = request.POST.get('priority')
            task_edit.start_time = request.POST.get('start_time')
            task_edit.deadline = request.POST.get('deadline')
            task_edit.complete = request.POST.get('complete')
            task_edit.save()
            return redirect('home')
        else:
            return render(request,'edit.html',{'task_edit' : task_edit })
    else:
        return redirect('error')
@login_required(login_url='login')
def delete(request,id_need_delete):
    task_delete = get_object_or_404(task, task_id=id_need_delete)
    if(request.method == 'GET'):
        task_delete.delete()
        return redirect('home')