from django.http import HttpResponse

def index(request):
    return HttpResponse('<a href="https://www.youtube.com/" > <h1>Youtube</h1> </a>')

def about(request):
    return HttpResponse('Hello About')