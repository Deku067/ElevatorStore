from django.shortcuts import render
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from .forms import UserRegistrationForm
from .models import UserProfile

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password']
            )
            
            # Check if the role is 'Admin' and set user as superuser and staff
            if form.cleaned_data['role'] == 'Admin':
                user.is_superuser = True
                user.is_staff = True
                user.save()
            
            UserProfile.objects.create(
                user=user,
                address=form.cleaned_data['address'],
                phone=form.cleaned_data['phone'],
                email_address=form.cleaned_data['email_address'],
                role=form.cleaned_data['role']
            )
            
            return redirect('login')  # Redirect to the login page after successful registration
    else:
        form = UserRegistrationForm()
    
    return render(request, 'core/register.html', {'form': form})



from django.contrib.auth import logout

def custom_logout_view(request):
    logout(request)
    return redirect('/')

