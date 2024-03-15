from django.contrib.auth.decorators import login_required
from main.models import task
from django.shortcuts import render
@login_required(login_url='login')
def home(request):
    userr = request.user
    taskk = task.objects.filter(who = userr.user_id)
    return render(request,'home.html',{'taskk' : taskk})