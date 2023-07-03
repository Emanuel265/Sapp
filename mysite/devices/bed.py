from django.http import HttpResponse


def index(request, command: str):
    match command:
        case "ON":
            print("Bed ON")
        case "OFF":
            print("Bed OFF")
    return HttpResponse(request)
