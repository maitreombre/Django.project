from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseRedirect
from django.urls import reverse
from django.views.generic.edit import CreateView
from .models import Task, Friend, Comment, CommonTask
from .forms import TaskForm, SignUpForm, CommonTaskForm
from django.contrib.auth.decorators import login_required


@login_required
def create_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.owner = request.user
            task.save()
            return redirect('my_tasks')
    else:
        form = TaskForm()
    return render(request, 'create_task.html', {'form': form})


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})


def home(request):
    return render(request, 'home.html')


@login_required
def profile(request):
    tasks = Task.objects.filter(owner=request.user)
    return render(request, 'profile.html', {'tasks': tasks})


@login_required
def add_friend(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        friend = get_object_or_404(User, username=username)
        if not Friend.objects.filter(user=request.user, friend=friend).exists() and not Friend.objects.filter(
                user=friend, friend=request.user, status=Friend.PENDING).exists():
            Friend.objects.create(user=request.user, friend=friend)
            messages.success(request, f"Friend request sent to {friend.username}.")
        next_url = request.GET.get('next', '/profile/friend_list/')
        return redirect(next_url)


@login_required
def accept_friend_request(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        friend = get_object_or_404(User, username=username)
        friend_request = Friend.objects.filter(user=friend, friend=request.user, status=Friend.PENDING).first()
        if friend_request:
            friend_request.status = Friend.APPROVED
            friend_request.save()
            Friend.objects.create(user=request.user, friend=friend, status=Friend.APPROVED)
            messages.success(request, f"You are now friends with {friend.username}.")
        next_url = request.GET.get('next', '/profile/friend_list/')
        return redirect(next_url)


@login_required
def decline_friend_request(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        friend = get_object_or_404(User, username=username)
        friend_request = Friend.objects.filter(user=friend, friend=request.user, status=Friend.PENDING).first()
        if friend_request:
            friend_request.delete()
            messages.success(request, f"You declined the friend request from {friend.username}.")
        next_url = request.GET.get('next', '/profile/friend_list/')
        return redirect(next_url)


@login_required
def remove_friend(request):
    if request.method == 'POST':
        friend_username = request.POST.get('friend_username')
        friend = get_object_or_404(User, username=friend_username)
        Friend.objects.filter(user=request.user, friend=friend).delete()
        Friend.objects.filter(user=friend, friend=request.user).delete()
        return redirect('friend_list')
    return render(request, 'friend_list.html')


@login_required
def friend_list(request):
    friends = Friend.objects.filter(user=request.user, status=Friend.APPROVED)
    friend_requests = Friend.objects.filter(friend=request.user, status=Friend.PENDING)
    return render(request, 'friend_list.html', {'friends': friends, 'friend_requests': friend_requests})


@login_required
def my_tasks(request):
    tasks = Task.objects.filter(owner=request.user).exclude(id__in=CommonTask.objects.all().values_list('id', flat=True))
    return render(request, 'my_tasks.html', {'tasks': tasks})


@login_required
def task_info(request, task_id):
    task = Task.objects.get(pk=task_id)
    context = {
        'task': task
    }
    return render(request, 'task_info.html', context)


@login_required
def task_comments(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    comments = Comment.objects.filter(task=task)
    context = {
        'task': task,
        'comments': comments
    }
    return render(request, 'task_comments.html', context)


@login_required
def add_comment(request):
    if request.method == 'POST':
        creator_id = request.user.id
        comment = request.POST.get('comment')
        task_id = request.POST.get('task_id')
        task = Task.objects.get(id=task_id)
        comment = Comment.objects.create(comment=comment, task=task, creator_id=creator_id)
        return redirect('task_comments', task_id=task.id)
    return render(request, 'task_comments.html')


@login_required
def delete_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    task_id = comment.task.id
    comment.delete()
    return redirect('task_comments', task_id=task_id)


@login_required
def create_common_task(request):
    if request.method == 'POST':
        form = CommonTaskForm(request.POST, user=request.user)
        if form.is_valid():
            task = form.save(commit=False)
            task.owner = request.user
            task.save()
            form.save_m2m()
            return redirect('common_tasks')
    else:
        form = CommonTaskForm(user=request.user)
    return render(request, 'create_common_task.html', {'form': form})


@login_required
def common_tasks(request):
    user_created_common_tasks = CommonTask.objects.all().values_list('id', flat=True)
    user_shared_common_tasks = CommonTask.objects.filter(shared_with=request.user)
    context = {
        'created_common_tasks': user_created_common_tasks,
        'shared_common_task': user_shared_common_tasks
    }
    return render(request, 'common_tasks.html', context)




