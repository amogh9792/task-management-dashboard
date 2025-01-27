# task_app/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .forms import LoginForm

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('admin_dashboard')  # Redirect to admin_dashboard after successful login
        else:
            messages.error(request, 'Invalid credentials, please try again.')

    return render(request, 'task_app/login_page.html')

def admin_dashboard(request):
    return render(request, 'task_app/admin_dashboard.html')