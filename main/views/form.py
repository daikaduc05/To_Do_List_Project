from main.models import task
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.shortcuts import render,redirect,get_object_or_404
@login_required(login_url='login')
def form(request,type,task_Id):
    userr = request.user
    content = {
        'type' : type 
    }
    if(type == 'Edit'):
        this_task = get_object_or_404(task,task_id = task_Id)
        content['this_task'] = this_task
     
    if request.method == 'POST' :
        description = request.POST['description']
        priority = request.POST['priority']
        start_time = request.POST['start_time']
        deadline = request.POST['deadline']
        complete = request.POST['complete']
        if(type == 'Create'):
            task.objects.create(
                who_id = userr.user_id,
                description = description,
                priority = priority,
                start_time = start_time,
                deadline = deadline,
                creat_at = timezone.now()
            )
        elif(type == 'Edit'):
            this_task.description = description
            this_task.priority = priority
            this_task.start_time = start_time
            this_task.deadline = deadline
            this_task.complete = complete
            this_task.save()
        return redirect('home')
    else:
        return render(request,'form.html',content)