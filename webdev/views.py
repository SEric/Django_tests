from django.http import HttpResponse


def index(request):
    output = "Hi!"
    return HttpResponse(output)
