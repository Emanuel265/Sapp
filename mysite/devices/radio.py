from django.http import HttpResponse


def index(request, command: str):
    match command:
        case "ON":
            print("Radio ON")
        case "OFF":
            print("Radio OFF")
    return HttpResponse(request)
