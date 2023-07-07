from django.http import HttpResponse


def index(request, command: str):
    print("Remote OFF")
    return HttpResponse(request)
