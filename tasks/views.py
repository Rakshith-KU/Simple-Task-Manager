from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import Task
from .forms import TaskForm
from datetime import timedelta

#  Show list of tasks + dashboard
@login_required
def task_list(request):
    tasks = Task.objects.filter(user=request.user).order_by('deadline')
    now = timezone.localtime(timezone.now())


    # Stats
    total_tasks = tasks.count()
    completed_tasks = tasks.filter(completed=True).count()
    pending_tasks = tasks.filter(completed=False).count()

    # Next due task
    next_due = tasks.filter(completed=False, deadline__gte=now).order_by('deadline').first()
    time_left = None
    if next_due:
        delta = next_due.deadline - now
        if delta.days >= 1:
            time_left = f"{delta.days} day{'s' if delta.days > 1 else ''} left"
        else:
            hours = delta.seconds // 3600
            mins = (delta.seconds % 3600) // 60
            time_left = f"{hours}h {mins}m left"

    return render(request, 'tasks/task_list.html', {
        'tasks': tasks,
        'now': now,
        'total_tasks': total_tasks,
        'completed_tasks': completed_tasks,
        'pending_tasks': pending_tasks,
        'next_due': next_due,
        'time_left': time_left,
    })


#  Create a new task
@login_required
def task_create(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            return redirect('task_list')
    else:
        form = TaskForm()
    return render(request, 'tasks/create_task.html', {'form': form})


#  Edit a task
@login_required
def task_edit(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm(instance=task)
    return render(request, 'tasks/create_task.html', {'form': form})


#  Delete a task
@login_required
def task_delete(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)
    if request.method == 'POST':
        task.delete()
        return redirect('task_list')
    return render(request, 'tasks/delete_task.html', {'task': task})


#  Toggle completion status
@login_required
def task_toggle_status(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)
    task.completed = not task.completed
    task.save()
    return redirect('task_list')
