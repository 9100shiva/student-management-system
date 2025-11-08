from django.shortcuts import render, redirect
from signup.models import sms4
from django.contrib.auth.models import User
from django.contrib import messages

def signup(request):
    if request.method == "POST":
        FullName = request.POST.get('FullName').strip()
        Email = request.POST.get('Email').strip()
        Username = request.POST.get('Username').strip()
        Password = request.POST.get('Password').strip()
        Role = request.POST.get('Role').strip()

        # Check if any field is empty
        if not FullName or not Email or not Username or not Password or not Role:
            messages.error(request, "All fields are required!")
            return redirect('signup')

        # Check if email already exists
        if User.objects.filter(username=Email).exists():
            messages.error(request, 'Email already exists. Please log in instead.')
            return redirect('login')

        # Check if Username already exists in your custom table
        if sms4.objects.filter(Username=Username).exists():
            messages.error(request, 'Username already taken. Please choose another.')
            return redirect('signup')

        try:
            # Create the user (email as username)
            user = User.objects.create_user(username=Email, email=Email, password=Password)
            user.save()

            # Create entry in custom table
            sms4.objects.create(
                FullName=FullName,
                Email=Email,
                Username=Username,
                Role=Role
            )

            messages.success(request, 'Account created successfully. Please log in.')
            return redirect('login')

        except Exception as e:
            messages.error(request, f"Error creating account: {str(e)}")
            return redirect('signup')

    return render(request, 'signup.html')


# Logout view
from django.contrib.auth import logout

def logout_view(request):
    logout(request)
    return redirect('login')
