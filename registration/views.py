from django.contrib.auth import login, authenticate, views
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect


from registration.registrationForm import registrationForm

def register(request):
    if request.user.is_authenticated:
        return redirect('gardens')
    else:
        if request.method == 'POST':
            form = registrationForm(request.POST)
            if form.is_valid():
                form.save()
                username = form.cleaned_data.get('username')
                raw_password = form.cleaned_data.get('password1')
                user = authenticate(username=username, password=raw_password)
                login(request, user)
                return redirect('gardens')
        else:
            form = registrationForm()
        return render(request, 'registration/register.html', {'form': form})

def mylogin(request):
    if request.user.is_authenticated:
        return redirect('gardens')
    else:
        return views.LoginView.as_view(request)
