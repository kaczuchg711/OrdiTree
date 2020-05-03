from django.http import HttpResponse
from django.template import loader

# Create your views here.
def index(request):
    template = loader.get_template('.\login\index.html')
    context = {}
    return HttpResponse(template.render(context, request))

def LoginPage(request):
    template = "LoginPage.html"
    context = {}
    return render(request,template,context)