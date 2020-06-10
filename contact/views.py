from django.shortcuts import render
from contact.forms import MessageOrdiTreeForm
from contact.models import MessageOrdiTree
from django.contrib.auth.models import User
import datetime

# Create your views here.
def contactPanel(request):

    readMessage = MessageOrdiTree.objects.filter(reciever=request.user.id)
    userMessages= {}
    for i in readMessage:
        userMessages[i.sender] = i.message_content

    form = MessageOrdiTreeForm(request.POST or None)
    messageModel=MessageOrdiTree()
    if 'reciever' in request.POST and 'message_content' in request.POST:
        messageModel.reciever = User.objects.get(id=request.POST['reciever'])
        messageModel.sender = request.user
        messageModel.message_content = request.POST['message_content']
        messageModel.created = datetime.datetime.now()
        messageModel.save()
        sprawdzenie = 'jestem w ifie'
    else:
        sprawdzenie = 'nie ma mnie w ifie'

    context = {
        'sprawdzenie':sprawdzenie,
        "user_id": request.user.id,
        'form': form,
        'yourmessages':userMessages,
    }
    if not context.get("user_id", False):
        return render(request, "registration/nonePermission.html", context)

    return render(request, "contact.html", context)
