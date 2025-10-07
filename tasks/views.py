from django.shortcuts import render
from .models import Task

def task_list(request):
    tasks = Task.objects.all().order_by('deadline')
    return render(request, 'tasks/task_list.html', {'tasks': tasks})

from django.shortcuts import render, redirect
from .forms import TaskForm

def create_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user  # assign current user
            task.save()
            return redirect('task_list')
    else:
        form = TaskForm()
    return render(request, 'tasks/create_task.html', {'form': form})

