from django.shortcuts import redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from main.models import task
@login_required(login_url='login')
def delete(request,id_need_delete):
    task_delete = get_object_or_404(task, task_id=id_need_delete)
    if(request.method == 'GET'):
        task_delete.delete()
        return redirect('home')