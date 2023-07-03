from django.http import HttpResponse


def index(request, command: str):
    match command:
        case "ON":
            print("Remote ON")
        case "OFF":
            print("Remote OFF")
    return HttpResponse(request)
