from django.shortcuts import render
from userPanel.changeUserDataForm import changeUserData
from django.contrib.auth.models import User
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
    return render(request,"userPanel.html", {'form': form} )