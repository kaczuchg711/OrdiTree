from django.shortcuts import render, redirect
from userPanel.changeUserDataForm import changeUserData
from django.contrib.auth.models import User
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages
# Create your views here.

def userPanel(request):
    context = {
        "user_id": request.user.id
    }
    if not context.get("user_id", False):
        return render(request, "registration/nonePermission.html", context)
    
    if request.method == 'POST':
        form = changeUserData(request.POST, instance=request.user)
        if form.is_valid():
            print("OK")
            #user = User.objects.all().filter(id_user = request.user.id)
            #user.email
            request.user.email = form.cleaned_data.get('email')
            request.user.username = form.cleaned_data.get('username')
            request.user.save()
        
    form = changeUserData(instance=request.user)
    return render(request,"userPanel/userPanel.html", {'form': form} )

def changePassword(request):
    context = {
        "user_id": request.user.id
    }
    if not context.get("user_id", False):
        return render(request, "registration/nonePermission.html", context)

    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('userPanel')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'userPanel/changePassword.html', {
        'form': form
    })