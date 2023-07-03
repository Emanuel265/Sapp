from django.http import HttpResponse


def index(request, command: str):
    match command:
        case "ON":
            print("Light ON")
        case "OFF":
            print("Light OFF")
    return HttpResponse(request)
