from django.http import HttpResponse


def index(request, command: str):
    match command:
        case "ON":
            print("Command ON")
        case "OFF":
            print("Command OFF")
    return HttpResponse(request)
