from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def home(request):
    # Show the login page
    return render(request, 'home.html')

def login_users(request):
    if request.method == "POST":
        first_name = request.POST['first_name']
        password = request.POST['password']

        # Authenticate user
        user = authenticate(request, username=first_name, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, f"Welcome, {first_name}!")
            return redirect('home')  # after login success
        else:
            messages.error(request, "Invalid first name or password.")
            return redirect('login')  # reload login form
    else:
        return render(request, 'home.html')

def logout_user(request):
    logout(request)
    messages.info(request, "You have been logged out.")
    return redirect('login')


from django.shortcuts import render

def _user(request):
    return render(request, 'register.html')
