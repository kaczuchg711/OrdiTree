from django.shortcuts import render

# Create your views here.
def contactPanel(request):

    readMessage = MessageOrdiTree.objects.filter(reciever=request.user)
    sendMessage = Message.objects.filter(sender = request.user)
    context = {
        "user_id": request.user.id
    }
    if not context.get("user_id", False):
        return render(request, "registration/nonePermission.html", context)

    return render(request, "contact.html", context)