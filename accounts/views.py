from django.shortcuts import render, redirect

def register(request):
    if request.method == 'POST':
        # Reigster User
        pass
    else:
        return render(request, 'accounts/register.html')

def login(request):
    if request.method == 'POST':
        # Login User
        pass
    else:
        return render(request, 'accounts/login.html')

def logout(request):
    return render(request, 'index')

def dashboard(request):
    return render(request, 'accounts/dashboard.html')
