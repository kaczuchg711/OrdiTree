from django.shortcuts import render
from contact.forms import MessageOrdiTreeForm
from contact.models import MessageOrdiTree
# Create your views here.
def contactPanel(request):

    readMessage = MessageOrdiTree.objects.filter(reciever=request.user)
    sendMessage = MessageOrdiTree.objects.filter(sender = request.user)
    form = MessageOrdiTreeForm()
    context = {
        "user_id": request.user.id,
        'form': form,
        'yourmessages':readMessage,
        'sendersmessages':sendMessage
    }
    if not context.get("user_id", False):
        return render(request, "registration/nonePermission.html", context)

    return render(request, "contact.html", context)
